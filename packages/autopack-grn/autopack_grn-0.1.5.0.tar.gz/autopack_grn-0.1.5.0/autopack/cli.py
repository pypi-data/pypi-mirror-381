import argparse
import os
import sys
import json
import gc
from typing import List, Optional, Tuple, Dict

import torch
from . import __version__
from .quantize import quantize_to_hf
from .exporters import export_onnx, export_gguf
from .publish import publish_folder_to_hub
from .scan import scan_model, print_scan_report
from .evaluation import calculate_perplexity, benchmark_hf, benchmark_onnx, benchmark_gguf
from transformers.utils import logging as hf_logging
from huggingface_hub import snapshot_download
from transformers import AutoConfig, BitsAndBytesConfig
from tqdm import tqdm
from .state import PipelineState


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="autopack",
        description="Quantize and publish Hugging Face models in multiple formats.",
    )

    # Global flags
    parser.add_argument("--version", action="version", version=f"autopack {__version__}")

    subparsers = parser.add_subparsers(dest="command", required=False)

    # auto command (default): run 4 quantization variants and summarize sizes/speedups
    a = subparsers.add_parser("auto", help="Run 4 quant variants and print a summary table")
    a.add_argument("--verbose", action="store_true", help="Enable verbose logs")
    a.add_argument("model", help="Hugging Face repo id (user/model) or local path")
    a.add_argument(
        "-o",
        "--output-dir",
        default=None,
        help="Base directory to write the quantized model variants (default: derived from model)",
    )
    a.add_argument(
        "--output-format",
        nargs="+",
        choices=["hf", "onnx", "gguf"],
        default=["hf"],
        help="One or more output formats to produce (gguf is opt-in)",
    )
    a.add_argument(
        "--device",
        choices=["auto", "cpu", "cuda"],
        default="auto",
        help="Device to use for benchmarking and evaluation (auto/cpu/cuda)",
    )
    a.add_argument(
        "--trust-remote-code",
        action="store_true",
        help="Allow custom code from model repos",
    )
    a.add_argument(
        "--revision",
        default=None,
        help="Model revision/branch/tag to load (for Hub models)",
    )
    a.add_argument(
        "--eval-dataset",
        default=None,
        help="Optional Hugging Face dataset to run perplexity evaluation on (e.g., wikitext-2-raw-v1)",
    )
    a.add_argument(
        "--eval-text-key",
        default="text",
        help="Column name in the eval dataset containing raw text",
    )
    a.add_argument(
        "--gguf-converter",
        default=None,
        help="Path to llama.cpp convert.py (or set LLAMA_CPP_CONVERT)",
    )
    a.add_argument(
        "--gguf-quant",
        nargs="+",
        default=None,
        help="One or more llama.cpp quant presets (e.g., Q4_K_M Q5_K_M)",
    )
    a.add_argument(
        "--gguf-extra-arg",
        dest="gguf_extra_args",
        action="append",
        default=None,
        help="Additional arguments for convert.py (repeatable)",
    )
    a.add_argument(
        "--gguf-no-isolation",
        action="store_true",
        help="Do not use an isolated virtualenv for GGUF conversion",
    )
    a.add_argument(
        "--gguf-force",
        action="store_true",
        help="Bypass architecture support check for GGUF conversion",
    )
    a.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip work for outputs that already exist",
    )
    a.add_argument(
        "--plan",
        action="store_true",
        help="Print a dry-run plan with resource estimates and exit",
    )
    a.add_argument(
        "--resume",
        action="store_true",
        help="Resume from .autopack_state.json and skip completed steps",
    )
    a.add_argument(
        "--force-step",
        nargs="+",
        default=None,
        help="One or more step ids to force re-run (e.g., hf:bnb-4bit gguf:Q4_K_M)",
    )
    a.add_argument(
        "--summary-json",
        action="store_true",
        help="Write machine-readable summary.json alongside README",
    )
    a.add_argument("--bench", action="store_true", help="Benchmark generated variants to report tokens/s (default: on)")
    a.add_argument("--no-bench", action="store_true", help="Disable benchmarking and use heuristic estimates instead")
    a.add_argument("--bench-prompt", default="Hello world", help="Prompt used for benchmarking")
    a.add_argument("--bench-max-new-tokens", type=int, default=16, help="Max new tokens for benchmarking (auto)")
    a.add_argument("--bench-warmup", type=int, default=0, help="Number of warmup runs for benchmarking (auto)")
    a.add_argument("--bench-runs", type=int, default=1, help="Number of timed runs for benchmarking (auto)")
    a.add_argument(
        "--hf-variants",
        nargs="+",
        choices=["bnb-4bit", "bnb-8bit", "int8-dynamic", "bf16"],
        default=None,
        help="Limit which HF variants to produce (default: all)",
    )
    a.add_argument(
        "--hf-variant",
        choices=["bnb-4bit", "bnb-8bit", "int8-dynamic", "bf16"],
        default=None,
        help="Produce a single HF variant (convenience alias for --hf-variants <one>)",
    )
    a.add_argument(
        "--max-memory-gb",
        type=float,
        default=None,
        help="Maximum memory usage in GB (will skip variants that would exceed this limit)",
    )
    a.add_argument(
        "--memory-safe",
        action="store_true",
        help="Enable memory-safe mode (process one variant at a time with aggressive cleanup)",
    )
    a.add_argument(
        "--skip-int8-dynamic",
        action="store_true",
        help="Skip int8-dynamic quantization (requires more memory than other variants)",
    )

    # quantize command
    q = subparsers.add_parser("quantize", help="Quantize a model and export in chosen formats")
    q.add_argument("--verbose", action="store_true", help="Enable verbose logs")
    q.add_argument("model", help="Hugging Face repo id (user/model) or local path")
    q.add_argument(
        "--revision",
        default=None,
        help="Model revision/branch/tag to load (for Hub models)",
    )
    q.add_argument(
        "-o",
        "--output-dir",
        default=None,
        help="Directory to write the exported model(s) (default: derived from model)",
    )
    q.add_argument(
        "--quantization",
        choices=["bnb-4bit", "bnb-8bit", "int8-dynamic", "none"],
        default="bnb-4bit",
        help="Quantization strategy (bnb 4/8-bit or PyTorch int8-dynamic)",
    )
    q.add_argument(
        "--dtype",
        choices=["auto", "float16", "bfloat16", "float32"],
        default="bfloat16",
        help="Compute dtype for 4/8-bit layers (where applicable)",
    )
    q.add_argument(
        "--device-map",
        default="auto",
        help="Device map to use when loading the model (e.g., 'auto', 'cpu')",
    )
    q.add_argument(
        "--prune",
        type=float,
        default=0.0,
        help="Global magnitude pruning ratio (0..0.95)",
    )
    q.add_argument(
        "--trust-remote-code",
        action="store_true",
        help="Allow custom code from model repos",
    )
    q.add_argument(
        "--output-format",
        nargs="+",
        choices=["hf", "onnx", "gguf"],
        default=["hf"],
        help="One or more output formats to produce",
    )
    q.add_argument(
        "--gguf-converter",
        default=None,
        help="Path to llama.cpp convert.py (or set LLAMA_CPP_CONVERT)",
    )
    q.add_argument(
        "--gguf-quant",
        default=None,
        help="Optional llama.cpp quant preset (e.g., Q4_K_M, Q5_K_M)",
    )
    q.add_argument(
        "--gguf-extra-arg",
        dest="gguf_extra_args",
        action="append",
        default=None,
        help="Additional arguments for convert.py (repeatable)",
    )
    q.add_argument(
        "--gguf-no-isolation",
        action="store_true",
        help="Do not use an isolated virtualenv for GGUF conversion",
    )
    q.add_argument(
        "--gguf-force",
        action="store_true",
        help="Bypass architecture support check for GGUF conversion",
    )
    q.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip work for outputs that already exist",
    )
    q.add_argument(
        "--plan",
        action="store_true",
        help="Print a dry-run plan with resource estimates and exit",
    )
    q.add_argument(
        "--resume",
        action="store_true",
        help="Resume from .autopack_state.json and skip completed steps",
    )
    q.add_argument(
        "--force-step",
        nargs="+",
        default=None,
        help="One or more step ids to force re-run (e.g., hf gguf:Q4_K_M)",
    )

    # publish command
    p = subparsers.add_parser("publish", help="Publish an exported model folder to the Hugging Face Hub")
    p.add_argument("--verbose", action="store_true", help="Enable verbose logs")
    p.add_argument("folder", help="Local folder with model files to publish")
    p.add_argument("repo", help="Destination repo id, e.g., user/model")
    p.add_argument("--token", default=os.environ.get("HUGGINGFACE_HUB_TOKEN"), help="HF token (or set HUGGINGFACE_HUB_TOKEN)")
    p.add_argument("--private", action="store_true", help="Create/use a private repository")
    p.add_argument("--branch", default=None, help="Target branch (revision)")
    p.add_argument("--commit-message", default="Add model artifacts via autopack", help="Commit message")
    p.add_argument("--no-create", action="store_true", help="Do not attempt to create the repo if missing")

    # scan command
    s = subparsers.add_parser("scan", help="Inspect a model or folder and suggest export options")
    s.add_argument("--verbose", action="store_true", help="Enable verbose logs")
    s.add_argument("model", help="Hugging Face repo id (user/model) or local path")
    s.add_argument("--revision", default=None, help="Model revision/branch/tag to load (for Hub models)")
    s.add_argument("--trust-remote-code", action="store_true", help="Allow custom code from model repos")
    s.add_argument("--local-files-only", action="store_true", help="Do not make network calls when loading config/tokenizer")
    s.add_argument("--resolve-cache", action="store_true", help="Resolve the model to a local snapshot for file listing/size")
    s.add_argument("--json", dest="as_json", action="store_true", help="Print JSON output")
    s.add_argument("--show-files", action="store_true", help="List top files by size when local or cached")
    s.add_argument("--limit-files", type=int, default=50, help="Limit number of files to list with --show-files")

    # bench command
    b = subparsers.add_parser("bench", help="Benchmark model runtime(s) for latency and throughput")
    b.add_argument("--verbose", action="store_true", help="Enable verbose logs")
    b.add_argument("target", help="Path to exported folder or model id/path. For GGUF, pass path to .gguf file.")
    b.add_argument(
        "--backend",
        nargs="+",
        choices=["hf", "onnx", "gguf"],
        default=["hf"],
        help="One or more backends to benchmark",
    )
    b.add_argument("--prompt", default="Hello world", help="Prompt text to generate from")
    b.add_argument("--max-new-tokens", type=int, default=64, help="Max new tokens to generate for timing")
    b.add_argument("--device", default="auto", help="Device selection for HF/ONNX (auto/cpu/cuda)")
    b.add_argument("--num-warmup", type=int, default=1, help="Number of warmup runs")
    b.add_argument("--num-runs", type=int, default=3, help="Number of timed runs")
    b.add_argument("--trust-remote-code", action="store_true", help="Allow custom modeling code (HF backend)")
    b.add_argument("--llama-cli", default=None, help="Path to llama-cli for GGUF (optional)")

    # If invoked with no arguments, show help and exit
    if argv is None and len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    return parser.parse_args(argv)


def _generate_readme(
    base_model_id: str,
    output_dir: str,
    results: List[Tuple[str, str, int]],
    baseline_size: int,
    est_speed: dict,
    est_quality_drop: dict,
    perplexities: Dict[str, float],
):
    """Generate a README.md file in the output directory with a summary and code snippets."""
    readme_path = os.path.join(output_dir, "README.md")
    lines = [
        f"# Quantized Variants of `{base_model_id}`\n\n",
        "This directory contains multiple quantized versions of the base model, generated by the `autopack` tool.\n\n",
        "## Summary\n",
    ]

    # If summary.json/metrics include real tokens/s, reflect that; otherwise, keep estimated columns
    have_real = any(isinstance(v, dict) for v in est_speed.values()) if est_speed else False
    if perplexities:
        if have_real:
            lines.append(
                "| Variant | Output Path | Size | Rel Size | Tokens/s | Speedup vs bf16 | Perplexity |\n"
            )
            lines.append("|---|---|---:|---:|---:|---:|---:|\n")
        else:
            lines.append(
                "| Variant | Output Path | Size | Rel Size | Est Speedup | Est. Quality Drop | Perplexity |\n"
            )
            lines.append("|---|---|---:|---:|---:|---:|---:|\n")
    else:
        if have_real:
            lines.append(
                "| Variant | Output Path | Size | Rel Size | Tokens/s | Speedup vs bf16 |\n"
            )
            lines.append("|---|---|---:|---:|---:|---:|\n")
        else:
            lines.append(
                "| Variant | Output Path | Size | Rel Size | Est Speedup | Est. Quality Drop |\n"
            )
            lines.append("|---|---|---:|---:|---:|---:|\n")

    for name, out_dir, sz in results:
        rel = sz / baseline_size if baseline_size else 1.0
        size_h = _human_size(sz)
        metric = est_speed.get(name, 1.0)
        quality = est_quality_drop.get(name, "N/A")
        # Use relative paths for the README
        relative_path = os.path.relpath(out_dir, output_dir)
        if isinstance(metric, dict):
            tps = metric.get("tokens_per_s", 0.0)
            speedup = metric.get("speedup_vs_bf16", 1.0)
            if perplexities:
                ppl = perplexities.get(name)
                ppl_str = f"{ppl:.4f}" if ppl else "N/A"
                lines.append(
                    f"| {name} | `{relative_path}` | {size_h} | {rel:.2f} | {tps:.2f} | {speedup:.2f}x | {ppl_str} |\n"
                )
            else:
                lines.append(
                    f"| {name} | `{relative_path}` | {size_h} | {rel:.2f} | {tps:.2f} | {speedup:.2f}x |\n"
                )
        else:
            speed = float(metric)
            if perplexities:
                ppl = perplexities.get(name)
                ppl_str = f"{ppl:.4f}" if ppl else "N/A"
                lines.append(
                    f"| {name} | `{relative_path}` | {size_h} | {rel:.2f} | {speed:.2f}x | {quality} | {ppl_str} |\n"
                )
            else:
                lines.append(
                    f"| {name} | `{relative_path}` | {size_h} | {rel:.2f} | {speed:.2f}x | {quality} |\n"
                )

    lines.append("\n## Usage\n")
    lines.append(
        "To load and use these models, you will need the `transformers` library and, for some variants, `bitsandbytes`.\n"
    )
    lines.append("```bash\npip install transformers accelerate safetensors bitsandbytes\n```\n\n")

    for name, out_dir, _ in results:
        relative_path = os.path.relpath(out_dir, output_dir)
        lines.append(f"### {name}\n")
        if name.startswith("gguf"):
            lines.append(
                "This model is in GGUF format and is designed to be used with `llama.cpp`.\n\n"
            )
            lines.append(
                "**Note**: You must have `llama.cpp` compiled and available on your system to run this model.\n\n"
            )
            lines.append("Example usage:\n")
            lines.append("```bash\n")
            lines.append(f'./main -m ./{relative_path} -n 128 -p "Once upon a time"\n')
            lines.append("```\n\n")
        else:
            lines.append("```python\n")
            lines.append("from transformers import AutoTokenizer, AutoModelForCausalLM\n\n")
            lines.append(f'model_path = "./{relative_path}"\n\n')
            lines.append("tokenizer = AutoTokenizer.from_pretrained(model_path)\n")
            lines.append(
                'model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)\n'
            )
            lines.append("```\n\n")

    with open(readme_path, "w") as f:
        f.writelines(lines)
    print(f"Generated summary README at: {readme_path}")


def _human_size(num_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(num_bytes)
    for unit in units:
        if size < 1024.0 or unit == units[-1]:
            return f"{size:.2f} {unit}"
        size /= 1024.0


def _human_time(seconds: float) -> str:
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    if minutes <= 0:
        return f"{secs}s"
    hours = minutes // 60
    minutes = minutes % 60
    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m {secs}s"


def _gpu_total_vram_gb() -> Optional[float]:
    try:
        if torch.cuda.is_available():
            total = 0
            for i in range(torch.cuda.device_count()):
                props = torch.cuda.get_device_properties(i)
                total += getattr(props, "total_memory", 0)
            if total > 0:
                return float(total) / (1024**3)
    except Exception:
        pass
    return None


def _estimate_step_time_gb(size_gb: float, kind: str) -> float:
    """Very rough time estimate in seconds based on artifact size and step kind."""
    base = 60.0
    per_gb = 45.0
    if kind.startswith("gguf"):
        per_gb = 60.0
    if kind == "onnx":
        per_gb = 50.0
    return max(30.0, base + per_gb * max(size_gb, 0.1))


def _print_plan(rows: List[Dict[str, object]], totals: Dict[str, float]) -> None:
    headers = ("Step", "Downloads", "RAM/VRAM", "Temp Disk", "Est Time")
    print("\nPlanned steps (dry run):\n")
    print(f"{headers[0]:<20}  {headers[1]:>12}  {headers[2]:>14}  {headers[3]:>12}  {headers[4]:>10}")
    print("-" * 78)
    for r in rows:
        print(
            f"{r['step']:<20}  {r['download']:>12}  {r['memory']:>14}  {r['temp']:>12}  {r['time']:>10}"
        )
    print("-" * 78)
    print(
        f"{'TOTAL':<20}  {totals.get('download_h','-'):>12}  {totals.get('memory_h','-'):>14}  {totals.get('temp_h','-'):>12}  {totals.get('time_h','-'):>10}"
    )
    print()


def _dir_size(path: str) -> int:
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                total += os.path.getsize(fp)
            except OSError:
                pass
    return total


def run_auto(args: argparse.Namespace) -> int:
    os.makedirs(args.output_dir, exist_ok=True)

    # Derive HF variant plan based on requested device preference.
    # - On CPU, skip BitsAndBytes variants (GPU-only) and force device_map="cpu".
    # - On CUDA, keep the default mix with device_map="auto".
    # - On auto, keep the default mix.
    device_pref = getattr(args, "device", "auto")
    # Detect pre-quantized models to skip BNB variants
    is_pre_quantized = False
    try:
        cfg = AutoConfig.from_pretrained(
            args.model,
            revision=args.revision,
            trust_remote_code=args.trust_remote_code,
        )
        existing_qc = getattr(cfg, "quantization_config", None)
        is_pre_quantized = bool(existing_qc) and not isinstance(existing_qc, BitsAndBytesConfig)
    except Exception:
        pass

    # Base variants
    if device_pref == "cpu":
        base_variants: List[Tuple[str, dict]] = [
            ("int8-dynamic", {"quantization": "int8-dynamic", "dtype": "float32", "device_map": "cpu"}),
            ("bf16", {"quantization": "none", "dtype": "bfloat16", "device_map": "cpu"}),
        ]
    else:
        base_variants: List[Tuple[str, dict]] = [
            ("bnb-4bit", {"quantization": "bnb-4bit", "dtype": "bfloat16", "device_map": "auto"}),
            ("bnb-8bit", {"quantization": "bnb-8bit", "dtype": "auto", "device_map": "auto"}),
            ("int8-dynamic", {"quantization": "int8-dynamic", "dtype": "float32", "device_map": "cpu"}),
            ("bf16", {"quantization": "none", "dtype": "bfloat16", "device_map": "auto"}),
        ]

    # Filter by --hf-variants if provided
    if getattr(args, "hf_variants", None):
        wanted = set(args.hf_variants)
        base_variants = [(n, p) for (n, p) in base_variants if n in wanted]

    # Auto-skip BNB variants for pre-quantized models
    if is_pre_quantized:
        base_variants = [(n, p) for (n, p) in base_variants if n not in {"bnb-4bit", "bnb-8bit"}]

    # Skip int8-dynamic if requested (memory-intensive)
    if getattr(args, "skip_int8_dynamic", False):
        base_variants = [(n, p) for (n, p) in base_variants if n != "int8-dynamic"]
        print("Skipping int8-dynamic quantization (memory-intensive)")
    
    # Auto-skip int8-dynamic for large models when memory is limited
    if not getattr(args, "skip_int8_dynamic", False):
        try:
            import psutil
            available_gb = psutil.virtual_memory().available / (1024**3)
            # If less than 20GB available, skip int8-dynamic for 7B+ models
            if available_gb < 20.0:
                # Check if this looks like a large model (7B+)
                try:
                    from .quantize import _get_model_size_estimate
                    estimated_size = _get_model_size_estimate(args.model, local_files_only=False, quantization="int8-dynamic")
                    if estimated_size > 6.0:
                        base_variants = [(n, p) for (n, p) in base_variants if n != "int8-dynamic"]
                        print(f"Auto-skipping int8-dynamic quantization (requires ~{estimated_size:.1f}GB, only {available_gb:.1f}GB available)")
                except Exception:
                    pass  # If we can't estimate, continue anyway
        except ImportError:
            pass  # psutil not available, continue anyway

    variants: List[Tuple[str, dict]] = base_variants

    # Planner and resume state
    def _plan_for_auto(args_inner: argparse.Namespace, variants_inner: List[Tuple[str, dict]]):
        try:
            scan = scan_model(
                model_id_or_path=args_inner.model,
                revision=args_inner.revision,
                trust_remote_code=args_inner.trust_remote_code,
                local_files_only=True,
                resolve_cache=False,
            )
        except Exception:
            scan = {"sizes": {"weight_bytes": 0}}
        weight_bytes = int(((scan or {}).get("sizes") or {}).get("weight_bytes", 0))
        download_h = _human_size(weight_bytes)
        vram_total = _gpu_total_vram_gb()
        from .quantize import _get_model_size_estimate
        rows = []
        total_download = float(weight_bytes)
        total_temp = 0.0
        total_time = 0.0
        max_ram = 0.0
        for name, params in variants_inner:
            est_gb = float(_get_model_size_estimate(args_inner.model, local_files_only=True, quantization=params["quantization"]))
            mem_gb = est_gb * 1.5
            max_ram = max(max_ram, mem_gb)
            temp_bytes = int(est_gb * (1024**3) * 0.2)
            total_temp += temp_bytes
            t = _estimate_step_time_gb(est_gb, f"hf:{name}")
            total_time += t
            rows.append({
                "step": f"hf:{name}",
                "download": download_h if weight_bytes else "-",
                "memory": f"~{mem_gb:.1f} GB" + (f" (<= {vram_total:.1f} GB VRAM)" if vram_total else ""),
                "temp": _human_size(temp_bytes),
                "time": _human_time(t),
            })
        if "onnx" in args_inner.output_format:
            est_gb = float(_get_model_size_estimate(args_inner.model, local_files_only=True, quantization="none"))
            mem_gb = est_gb * 1.2
            max_ram = max(max_ram, mem_gb)
            temp_bytes = int(est_gb * (1024**3) * 0.1)
            total_temp += temp_bytes
            t = _estimate_step_time_gb(est_gb, "onnx")
            total_time += t
            rows.append({
                "step": "onnx",
                "download": download_h if weight_bytes else "-",
                "memory": f"~{mem_gb:.1f} GB",
                "temp": _human_size(temp_bytes),
                "time": _human_time(t),
            })
        if "gguf" in args_inner.output_format:
            quant_list = args_inner.gguf_quant if args_inner.gguf_quant else ["Q4_K_M", "Q5_K_M", "Q8_0"]
            for q in [q.upper() for q in quant_list]:
                est_gb = float(_get_model_size_estimate(args_inner.model, local_files_only=True, quantization="none"))
                mem_gb = est_gb
                max_ram = max(max_ram, mem_gb)
                temp_bytes = int(est_gb * (1024**3) * 0.25)
                total_temp += temp_bytes
                t = _estimate_step_time_gb(est_gb, f"gguf:{q}")
                total_time += t
                rows.append({
                    "step": f"gguf:{q}",
                    "download": download_h if weight_bytes else "-",
                    "memory": f"~{mem_gb:.1f} GB",
                    "temp": _human_size(temp_bytes),
                    "time": _human_time(t),
                })
        totals = {
            "download_h": download_h if weight_bytes else "-",
            "memory_h": f"~{max_ram:.1f} GB",
            "temp_h": _human_size(int(total_temp)),
            "time_h": _human_time(total_time),
        }
        _print_plan(rows, totals)

    if getattr(args, "plan", False):
        _plan_for_auto(args, variants)
        return 0

    state = PipelineState(PipelineState.default_path(args.output_dir))
    planned_steps: List[str] = []
    if "hf" in args.output_format:
        planned_steps.extend([f"hf:{name}" for name, _ in variants])
    if "onnx" in args.output_format:
        planned_steps.append("onnx")
    if "gguf" in args.output_format:
        quant_list = args.gguf_quant if args.gguf_quant else ["Q4_K_M", "Q5_K_M", "Q8_0"]
        planned_steps.extend([f"gguf:{q.upper()}" for q in quant_list])
    state.init_steps(planned_steps)
    force_steps = set(getattr(args, "force_step", []) or [])

    results = []
    perplexities: Dict[str, float] = {}

    # Progress total across requested outputs
    total_steps = 0
    if "hf" in args.output_format:
        total_steps += len(variants)
    if "onnx" in args.output_format:
        total_steps += 1
    if "gguf" in args.output_format:
        # Determine quant list early for progress accounting
        quant_list = args.gguf_quant if args.gguf_quant else ["Q4_K_M", "Q5_K_M", "Q8_0"]
        total_steps += len(quant_list)

    # Import the clean progress bar
    from .quantize import CleanProgressBar
    pbar = CleanProgressBar(total_steps, "autopack")
    pbar.start()

    # Resolve model to a local snapshot once to avoid repeated downloads for large models
    source_model = args.model
    try:
        if not os.path.isdir(args.model):
            pbar.set_description("Resolve model cache")
            source_model = snapshot_download(repo_id=args.model, revision=args.revision)
    except Exception:
        source_model = args.model

    # --- Run HF variants (opt-in for auto) ---
    if "hf" in args.output_format:
        for name, params in variants:
            out_dir = os.path.join(args.output_dir, name)
            os.makedirs(out_dir, exist_ok=True)
            step_id = f"hf:{name}"
            if getattr(args, "resume", False) and state.is_completed(step_id) and step_id not in force_steps:
                state.mark_skipped(step_id, "already completed")
                pbar.update_step(f"Skipping {name} (resume)")
                size_bytes = _dir_size(out_dir)
                results.append((name, out_dir, size_bytes))
                pbar.update(1)
                continue
            
            # Check memory constraints
            if getattr(args, "max_memory_gb", None):
                try:
                    import psutil
                    available_gb = psutil.virtual_memory().available / (1024**3)
                    if available_gb < args.max_memory_gb:
                        pbar.update_step(f"Skipping {name} (insufficient memory)")
                        results.append((name, out_dir, 0))
                        pbar.update(1)
                        continue
                except ImportError:
                    pass  # psutil not available, continue anyway
            
            # Process variant
            try:
                state.mark_running(step_id, f"Processing {name}")
                pbar.update_step(f"Processing {name} variant...")
                quantize_to_hf(
                    model_id_or_path=source_model,
                    output_dir=out_dir,
                    quantization=params["quantization"],
                    dtype=params["dtype"],
                    device_map=params["device_map"],
                    trust_remote_code=args.trust_remote_code,
                    revision=args.revision,
                    # Hint downstream loader to avoid accidental CUDA use in integrations
                    local_files_only=True,
                )
                size_bytes = _dir_size(out_dir)
                results.append((name, out_dir, size_bytes))
                pbar.update_step(f"Completed {name} ({_human_size(size_bytes)})")
                state.mark_completed(step_id, output_path=out_dir)
            except Exception as e:
                pbar.update_step(f"Skipping {name} (error: {str(e)[:50]}...)")
                # Create empty directory entry to maintain progress tracking
                results.append((name, out_dir, 0))
                state.mark_failed(step_id, str(e))
            finally:
                # Force garbage collection between variants
                gc.collect()
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                
                # Additional cleanup in memory-safe mode
                if getattr(args, "memory_safe", False):
                    import time
                    time.sleep(1)  # Give system time to reclaim memory
            
            pbar.update(1)

            # Run perplexity evaluation if requested
            if args.eval_dataset:
                try:
                    if ":" in args.eval_dataset:
                        dataset_id, dataset_config = args.eval_dataset.split(":", 1)
                    else:
                        dataset_id, dataset_config = args.eval_dataset, None
                    print(f"Running perplexity evaluation for {name} on {dataset_id} ({dataset_config})...")
                    ppl = calculate_perplexity(
                        out_dir,
                        dataset_id,
                        dataset_config or "",
                        text_key=getattr(args, "eval_text_key", "text"),
                        device=getattr(args, "device", "auto"),
                        trust_remote_code=args.trust_remote_code,
                    )
                    perplexities[name] = ppl
                    print(f"  - Perplexity: {ppl:.4f}")
                except Exception as e:
                    print(f"  - Could not calculate perplexity: {e}")

    # --- Optional ONNX export for auto ---
    if "onnx" in args.output_format:
        pbar.update_step("Exporting ONNX...")
        onnx_dir = os.path.join(args.output_dir, "onnx")
        os.makedirs(onnx_dir, exist_ok=True)
        step_id = "onnx"
        if getattr(args, "resume", False) and state.is_completed(step_id) and step_id not in force_steps:
            state.mark_skipped(step_id, "already completed")
            size_bytes = _dir_size(onnx_dir)
            results.append(("onnx", onnx_dir, size_bytes))
            pbar.update(1)
        else:
            try:
                if not (getattr(args, "skip_existing", False) and os.path.isdir(onnx_dir) and _dir_size(onnx_dir) > 0):
                    export_onnx(
                        model_id_or_path=source_model,
                        output_dir=onnx_dir,
                        trust_remote_code=args.trust_remote_code,
                        revision=args.revision,
                    )
                size_bytes = _dir_size(onnx_dir)
                results.append(("onnx", onnx_dir, size_bytes))
                pbar.update_step(f"Completed ONNX ({_human_size(size_bytes)})")
                state.mark_completed(step_id, output_path=onnx_dir)
            except Exception as e:
                pbar.update_step(f"Skipping ONNX (error: {str(e)[:50]}...)")
                state.mark_failed(step_id, str(e))
            finally:
                pbar.update(1)

    # --- Optional GGUF variants for auto (opt-in) ---
    if "gguf" in args.output_format:
        gguf_out_dir = os.path.join(args.output_dir, "gguf")
        os.makedirs(gguf_out_dir, exist_ok=True)
        try:
            # For auto command, explicitly point to the vendored llama.cpp relative to this script's location
            cli_dir = os.path.dirname(os.path.abspath(__file__))
            repo_root = os.path.dirname(cli_dir)
            default_converter_path = os.path.join(repo_root, "third_party", "llama.cpp", "convert_hf_to_gguf.py")
            llama_cpp_bin = os.path.join(repo_root, "third_party", "llama.cpp", "build", "bin")
            env = os.environ.copy()
            env["PATH"] = f"{llama_cpp_bin}:{env['PATH']}"

            # Prefer bf16 local export if it exists; otherwise, use original model path
            bf16_out_dir = next((r[1] for r in results if r[0] == "bf16"), None)
            source_model_path = bf16_out_dir if bf16_out_dir else args.model

            # Determine quant list (normalize to uppercase)
            quant_list = args.gguf_quant if args.gguf_quant else ["Q4_K_M", "Q5_K_M", "Q8_0"]
            quant_list = [q.upper() for q in quant_list]

            for quant in quant_list:
                try:
                    step_id = f"gguf:{quant}"
                    if getattr(args, "resume", False) and state.is_completed(step_id) and step_id not in force_steps:
                        state.mark_skipped(step_id, "already completed")
                        size_bytes = _dir_size(gguf_out_dir)
                        results.append((f"gguf-{quant}", gguf_out_dir, size_bytes))
                        pbar.update(1)
                        continue
                    state.mark_running(step_id, f"Exporting GGUF {quant}")
                    pbar.update_step(f"Exporting GGUF {quant}...")
                    expected_file = os.path.join(gguf_out_dir, f"model-{quant}.gguf")
                    if getattr(args, "skip_existing", False) and os.path.isfile(expected_file):
                        pass
                    else:
                        export_gguf(
                            model_id_or_path=source_model_path,
                            output_dir=gguf_out_dir,
                            quant=quant,
                            converter_path=(args.gguf_converter or default_converter_path),
                            trust_remote_code=args.trust_remote_code,
                            revision=args.revision,
                            extra_args=args.gguf_extra_args,
                            env=env,
                            isolate_env=not args.gguf_no_isolation,
                            force=args.gguf_force,
                        )
                    # Use directory size to avoid errors if path is None or if multiple files are produced
                    size_bytes = _dir_size(gguf_out_dir)
                    results.append((f"gguf-{quant}", gguf_out_dir, size_bytes))
                    pbar.update_step(f"Completed GGUF {quant} ({_human_size(size_bytes)})")
                    state.mark_completed(step_id, output_path=gguf_out_dir)
                except Exception as e:
                    pbar.update_step(f"Skipping GGUF {quant} (error: {str(e)[:50]}...)")
                    state.mark_failed(step_id, str(e))
                finally:
                    pbar.update(1)
        except Exception as e:
            print(f"Skipping GGUF export due to an error: {e}")

    pbar.close()

    # No GGML export in this version

    # Establish baseline size (bf16)
    baseline = next((r for r in results if r[0] == "bf16"), None)
    baseline_size = baseline[2] if baseline else max((r[2] for r in results if r[2] > 0), default=1)

    # Optional benchmarking to compute real tokens/s and speedups
    bench_metrics: Dict[str, Dict[str, float]] = {}
    # Benchmark by default for `auto` unless explicitly disabled via --no-bench
    bench_enabled = not getattr(args, "no_bench", False)
    if bench_enabled:
        prompt = getattr(args, "bench_prompt", "Hello world")
        max_new = getattr(args, "bench_max_new_tokens", 64)
        warmup = getattr(args, "bench_warmup", 1)
        runs = getattr(args, "bench_runs", 2)

        # HF variants
        for name, out_dir, _ in results:
            if name in {"bnb-4bit", "bnb-8bit", "int8-dynamic", "bf16"}:
                try:
                    print(f"  - Benchmarking {name}...")
                    res = benchmark_hf(
                        model_id_or_path=out_dir,
                        prompt=prompt,
                        max_new_tokens=max_new,
                        device=args.device,
                        trust_remote_code=args.trust_remote_code,
                        num_warmup=warmup,
                        num_runs=runs,
                    )
                    tokens_per_s = float(res.get("tokens_per_s", 0.0))
                    new_tokens = float(res.get("new_tokens", max_new))
                    
                    if tokens_per_s > 0:
                        bench_metrics[name] = {
                            "tokens_per_s": tokens_per_s,
                            "new_tokens": new_tokens,
                        }
                        print(f"  - {name}: {tokens_per_s:.2f} tokens/s")
                    else:
                        print(f"  - {name}: Benchmark completed but no tokens generated")
                except Exception as e:
                    print(f"  - Benchmark failed for {name}: {str(e)[:100]}...")

        # ONNX
        onnx_dir = os.path.join(args.output_dir, "onnx")
        if os.path.isdir(onnx_dir):
            try:
                res = benchmark_onnx(
                    model_dir=onnx_dir,
                    prompt=prompt,
                    max_new_tokens=max_new,
                    device=args.device,
                    num_warmup=warmup,
                    num_runs=runs,
                )
                bench_metrics["onnx"] = {
                    "tokens_per_s": float(res.get("tokens_per_s", 0.0)),
                    "new_tokens": float(res.get("new_tokens", max_new)),
                }
            except Exception as e:
                print(f"  - Benchmark failed for onnx: {e}")

        # GGUF: benchmark a representative .gguf file if present
        gguf_dir = os.path.join(args.output_dir, "gguf")
        if os.path.isdir(gguf_dir):
            try:
                gguf_file = next((os.path.join(gguf_dir, n) for n in sorted(os.listdir(gguf_dir)) if n.endswith(".gguf")), None)
                if gguf_file:
                    res = benchmark_gguf(
                        gguf_model_path=gguf_file,
                        prompt=prompt,
                        max_new_tokens=max_new,
                        num_warmup=warmup,
                        num_runs=runs,
                    )
                    bench_metrics["gguf"] = {
                        "tokens_per_s": float(res.get("tokens_per_s", 0.0)),
                        "new_tokens": float(res.get("new_tokens", max_new)),
                    }
            except Exception as e:
                print(f"  - Benchmark failed for gguf: {e}")

    # Speedups vs bf16 (floats for printing)
    if bench_metrics:
        bf16_tps = bench_metrics.get("bf16", {}).get("tokens_per_s", 0.0)
        real_speedups: Dict[str, float] = {}
        for name, _out_dir, _sz in results:
            tps = bench_metrics.get(name, {}).get("tokens_per_s")
            if tps is None and name.startswith("gguf"):
                tps = bench_metrics.get("gguf", {}).get("tokens_per_s")
            if tps is None and name == "onnx":
                tps = bench_metrics.get("onnx", {}).get("tokens_per_s")
            if tps and bf16_tps > 0:
                real_speedups[name] = tps / bf16_tps
            elif tps and tps > 0:
                # If we have tokens/s but no bf16 baseline, use heuristic
                est_speed_heuristic = {
                    "bf16": 1.00,
                    "bnb-8bit": 1.50,
                    "bnb-4bit": 2.50,
                    "int8-dynamic": 1.20,
                    "gguf": 2.80,
                    "onnx": 1.50,
                }
                real_speedups[name] = est_speed_heuristic.get(name, 1.0)
    else:
        est_speed_heuristic = {
            "bf16": 1.00,
            "bnb-8bit": 1.50,
            "bnb-4bit": 2.50,
            "int8-dynamic": 1.20,
            "gguf": 2.80,
            "onnx": 1.50,
        }
        real_speedups = est_speed_heuristic

    # Prepare metrics for README: include tokens/s when available
    readme_speed: Dict[str, Dict[str, float] | float] = {}
    if bench_metrics:
        for name, _out_dir, _sz in results:
            tps = bench_metrics.get(name, {}).get("tokens_per_s")
            if tps is None and name.startswith("gguf"):
                tps = bench_metrics.get("gguf", {}).get("tokens_per_s")
            if tps is None and name == "onnx":
                tps = bench_metrics.get("onnx", {}).get("tokens_per_s")
            spd = real_speedups.get(name)
            if tps is not None and spd is not None:
                readme_speed[name] = {"tokens_per_s": tps, "speedup_vs_bf16": spd}
    else:
        readme_speed = real_speedups

    # Estimated quality drop (lower is better, very rough heuristics for now )
    est_quality_drop = {
        "bf16": "0.0%",
        "bnb-8bit": "~0.1-0.5%",
        "bnb-4bit": "~0.5-2.0%",
        "int8-dynamic": "~0.5-3.0%",
        "gguf": "~0.5-1.5%",  # For Q4_K_M
    }

    # Print table (tokens/s & real speedup if benchmarks were run)
    if perplexities:
        if bench_metrics:
            headers = ("Variant", "Output Path", "Size", "Rel Size", "Tokens/s", "Speedup vs bf16", "Perplexity")
            print("\nSummary of quantized variants:\n")
            print(f"{headers[0]:<14}  {headers[1]:<40}  {headers[2]:>12}  {headers[3]:>9}  {headers[4]:>12}  {headers[5]:>16}  {headers[6]:>12}")
            print("-" * 130)
        else:
            headers = ("Variant", "Output Path", "Size", "Rel Size", "Est Speedup", "Est. Quality Drop", "Perplexity")
            print("\nSummary of quantized variants:\n")
            print(f"{headers[0]:<14}  {headers[1]:<40}  {headers[2]:>12}  {headers[3]:>9}  {headers[4]:>12}  {headers[5]:>18}  {headers[6]:>12}")
            print("-" * 130)
    else:
        if bench_metrics:
            headers = ("Variant", "Output Path", "Size", "Rel Size", "Tokens/s", "Speedup vs bf16")
            print("\nSummary of quantized variants:\n")
            print(f"{headers[0]:<14}  {headers[1]:<40}  {headers[2]:>12}  {headers[3]:>9}  {headers[4]:>12}  {headers[5]:>16}")
            print("-" * 115)
        else:
            headers = ("Variant", "Output Path", "Size", "Rel Size", "Est Speedup", "Est. Quality Drop")
            print("\nSummary of quantized variants:\n")
            print(f"{headers[0]:<14}  {headers[1]:<40}  {headers[2]:>12}  {headers[3]:>9}  {headers[4]:>12}  {headers[5]:>18}")
            print("-" * 115)

    for name, out_dir, sz in results:
        rel = sz / baseline_size if baseline_size else 1.0
        size_h = _human_size(sz)
        if bench_metrics:
            tokens_per_s = bench_metrics.get(name, {}).get("tokens_per_s")
            if tokens_per_s is None and name.startswith("gguf"):
                tokens_per_s = bench_metrics.get("gguf", {}).get("tokens_per_s")
            if tokens_per_s is None and name == "onnx":
                tokens_per_s = bench_metrics.get("onnx", {}).get("tokens_per_s")
            speedup = real_speedups.get(name, 1.0)
            if perplexities:
                ppl = perplexities.get(name)
                ppl_str = f"{ppl:.4f}" if ppl else "N/A"
                print(f"{name:<14}  {out_dir:<40}  {size_h:>12}  {rel:>9.2f}  {tokens_per_s if tokens_per_s else 0.0:>12.2f}  {speedup:>16.2f}x  {ppl_str:>12}")
            else:
                print(f"{name:<14}  {out_dir:<40}  {size_h:>12}  {rel:>9.2f}  {tokens_per_s if tokens_per_s else 0.0:>12.2f}  {speedup:>16.2f}x")
        else:
            speed = real_speedups.get(name, 1.0)
            quality = est_quality_drop.get(name, "N/A")
            if perplexities:
                ppl = perplexities.get(name)
                ppl_str = f"{ppl:.4f}" if ppl else "N/A"
                print(f"{name:<14}  {out_dir:<40}  {size_h:>12}  {rel:>9.2f}  {speed:>12.2f}x  {quality:>18}  {ppl_str:>12}")
            else:
                print(f"{name:<14}  {out_dir:<40}  {size_h:>12}  {rel:>9.2f}  {speed:>12.2f}x  {quality:>18}")
    print()

    # Generate README.md and optional summary.json
    _generate_readme(
        args.model, args.output_dir, results, baseline_size, readme_speed, est_quality_drop, perplexities
    )
    if getattr(args, "summary_json", False):
        try:
            summary = []
            for name, out_dir, sz in results:
                entry = {
                    "variant": name,
                    "output_path": os.path.relpath(out_dir, args.output_dir),
                    "size_bytes": sz,
                    "relative_size": (sz / baseline_size) if baseline_size else 1.0,
                    "estimated_speedup": None if bench_metrics else real_speedups.get(name, 1.0),
                    "estimated_quality_drop": est_quality_drop.get(name, None),
                }
                if bench_metrics:
                    entry["tokens_per_s"] = bench_metrics.get(name, {}).get("tokens_per_s")
                    if entry["tokens_per_s"] is None and name.startswith("gguf"):
                        entry["tokens_per_s"] = bench_metrics.get("gguf", {}).get("tokens_per_s")
                    if entry["tokens_per_s"] is None and name == "onnx":
                        entry["tokens_per_s"] = bench_metrics.get("onnx", {}).get("tokens_per_s")
                    entry["speedup_vs_bf16"] = real_speedups.get(name)
                if perplexities:
                    entry["perplexity"] = perplexities.get(name)
                summary.append(entry)
            with open(os.path.join(args.output_dir, "summary.json"), "w") as f:
                json.dump({
                    "base_model": args.model,
                    "results": summary,
                }, f, indent=2)
            print(f"Wrote summary JSON at: {os.path.join(args.output_dir, 'summary.json')}")
        except Exception as e:
            print(f"Could not write summary.json: {e}")

    return 0


def run_quantize(args: argparse.Namespace) -> int:
    os.makedirs(args.output_dir, exist_ok=True)
    total_steps = ("hf" in args.output_format) + ("onnx" in args.output_format) + ("gguf" in args.output_format)
    # Planner
    if getattr(args, "plan", False):
        # Reuse auto planner with a single HF variant if requested
        variants: List[Tuple[str, dict]] = []
        if "hf" in args.output_format:
            variants.append((args.quantization if args.quantization != "none" else "bf16", {"quantization": args.quantization, "dtype": args.dtype, "device_map": args.device_map}))
        class _Args:
            pass
        _a = _Args()
        _a.model = args.model
        _a.revision = args.revision
        _a.trust_remote_code = args.trust_remote_code
        _a.output_format = args.output_format
        _a.gguf_quant = args.gguf_quant
        # Inline planner from run_auto
        try:
            scan = scan_model(
                model_id_or_path=_a.model,
                revision=_a.revision,
                trust_remote_code=_a.trust_remote_code,
                local_files_only=True,
                resolve_cache=False,
            )
        except Exception:
            scan = {"sizes": {"weight_bytes": 0}}
        weight_bytes = int(((scan or {}).get("sizes") or {}).get("weight_bytes", 0))
        download_h = _human_size(weight_bytes)
        vram_total = _gpu_total_vram_gb()
        from .quantize import _get_model_size_estimate
        rows = []
        total_temp = 0.0
        total_time = 0.0
        max_ram = 0.0
        for name, params in variants:
            est_gb = float(_get_model_size_estimate(_a.model, local_files_only=True, quantization=params["quantization"]))
            mem_gb = est_gb * 1.5
            max_ram = max(max_ram, mem_gb)
            temp_bytes = int(est_gb * (1024**3) * 0.2)
            total_temp += temp_bytes
            t = _estimate_step_time_gb(est_gb, f"hf:{name}")
            total_time += t
            rows.append({
                "step": f"hf:{name}",
                "download": download_h if weight_bytes else "-",
                "memory": f"~{mem_gb:.1f} GB" + (f" (<= {vram_total:.1f} GB VRAM)" if vram_total else ""),
                "temp": _human_size(temp_bytes),
                "time": _human_time(t),
            })
        if "onnx" in _a.output_format:
            est_gb = float(_get_model_size_estimate(_a.model, local_files_only=True, quantization="none"))
            mem_gb = est_gb * 1.2
            max_ram = max(max_ram, mem_gb)
            temp_bytes = int(est_gb * (1024**3) * 0.1)
            total_temp += temp_bytes
            t = _estimate_step_time_gb(est_gb, "onnx")
            total_time += t
            rows.append({
                "step": "onnx",
                "download": download_h if weight_bytes else "-",
                "memory": f"~{mem_gb:.1f} GB",
                "temp": _human_size(temp_bytes),
                "time": _human_time(t),
            })
        if "gguf" in _a.output_format:
            q = args.gguf_quant.upper() if isinstance(args.gguf_quant, str) else args.gguf_quant
            est_gb = float(_get_model_size_estimate(_a.model, local_files_only=True, quantization="none"))
            mem_gb = est_gb
            max_ram = max(max_ram, mem_gb)
            temp_bytes = int(est_gb * (1024**3) * 0.25)
            total_temp += temp_bytes
            t = _estimate_step_time_gb(est_gb, f"gguf:{q or 'f16'}")
            total_time += t
            rows.append({
                "step": f"gguf:{q or 'f16'}",
                "download": download_h if weight_bytes else "-",
                "memory": f"~{mem_gb:.1f} GB",
                "temp": _human_size(temp_bytes),
                "time": _human_time(t),
            })
        totals = {
            "download_h": download_h if weight_bytes else "-",
            "memory_h": f"~{max_ram:.1f} GB",
            "temp_h": _human_size(int(total_temp)),
            "time_h": _human_time(total_time),
        }
        _print_plan(rows, totals)
        return 0

    pbar = tqdm(total=total_steps, desc="autopack", unit="step", disable=(total_steps == 0))
    state = PipelineState(PipelineState.default_path(args.output_dir))
    planned_steps: List[str] = []
    if "hf" in args.output_format:
        planned_steps.append("hf")
    if "onnx" in args.output_format:
        planned_steps.append("onnx")
    if "gguf" in args.output_format:
        q = args.gguf_quant.upper() if isinstance(args.gguf_quant, str) else args.gguf_quant
        planned_steps.append(f"gguf:{q}" if q else "gguf")
    state.init_steps(planned_steps)
    force_steps = set(getattr(args, "force_step", []) or [])

    # Always produce HF format first when requested
    if "hf" in args.output_format:
        pbar.set_description("HF export")
        step_id = "hf"
        if getattr(args, "resume", False) and state.is_completed(step_id) and step_id not in force_steps:
            state.mark_skipped(step_id, "already completed")
        elif not (getattr(args, "skip_existing", False) and os.path.isdir(args.output_dir) and _dir_size(args.output_dir) > 0):
            state.mark_running(step_id, "HF export")
            quantize_to_hf(
                model_id_or_path=args.model,
                output_dir=args.output_dir,
                quantization=args.quantization,
                dtype=args.dtype,
                device_map=args.device_map,
                trust_remote_code=args.trust_remote_code,
                revision=args.revision,
                prune=args.prune,
            )
            state.mark_completed(step_id, output_path=args.output_dir)
        pbar.update(1)

    # Produce ONNX by exporting from the original model id/path (fresh load)
    if "onnx" in args.output_format:
        pbar.set_description("ONNX export")
        onnx_dir = os.path.join(args.output_dir, "onnx")
        os.makedirs(onnx_dir, exist_ok=True)
        step_id = "onnx"
        if getattr(args, "resume", False) and state.is_completed(step_id) and step_id not in force_steps:
            state.mark_skipped(step_id, "already completed")
        elif not (getattr(args, "skip_existing", False) and os.path.isdir(onnx_dir) and _dir_size(onnx_dir) > 0):
            state.mark_running(step_id, "ONNX export")
            export_onnx(
                model_id_or_path=args.model,
                output_dir=onnx_dir,
                trust_remote_code=args.trust_remote_code,
                revision=args.revision,
            )
            state.mark_completed(step_id, output_path=onnx_dir)
        pbar.update(1)

    # GGUF export (optional)
    if "gguf" in args.output_format:
        pbar.set_description("GGUF export")
        gguf_dir = os.path.join(args.output_dir, "gguf")
        os.makedirs(gguf_dir, exist_ok=True)
        quant_arg = (args.gguf_quant.upper() if isinstance(args.gguf_quant, str) else args.gguf_quant)
        expected_file = None
        if isinstance(quant_arg, str):
            expected_file = os.path.join(gguf_dir, f"model-{quant_arg}.gguf")
        elif quant_arg is None:
            expected_file = os.path.join(gguf_dir, "model-f16.gguf")
        step_id = f"gguf:{quant_arg}" if isinstance(quant_arg, str) else "gguf"
        if getattr(args, "resume", False) and state.is_completed(step_id) and step_id not in force_steps:
            state.mark_skipped(step_id, "already completed")
        elif not (getattr(args, "skip_existing", False) and expected_file and os.path.isfile(expected_file)):
            state.mark_running(step_id, "GGUF export")
            export_gguf(
                model_id_or_path=args.model,
                output_dir=gguf_dir,
                trust_remote_code=args.trust_remote_code,
                revision=args.revision,
                converter_path=args.gguf_converter,
                quant=quant_arg,
                extra_args=args.gguf_extra_args,
                isolate_env=not args.gguf_no_isolation,
                force=args.gguf_force,
            )
            state.mark_completed(step_id, output_path=gguf_dir)
        pbar.update(1)

    pbar.close()

    # No GGML export in this version

    return 0


def run_publish(args: argparse.Namespace) -> int:
    create = not args.no_create
    publish_folder_to_hub(
        folder=args.folder,
        repo_id=args.repo,
        token=args.token,
        private=args.private,
        commit_message=args.commit_message,
        revision=args.branch,
        create=create,
    )
    return 0


def _print_bench_results(rows):
    headers = ("Backend", "Latency (s)", "Tokens/s", "Device", "Max Mem")
    print("\nBenchmark results:\n")
    print(f"{headers[0]:<10}  {headers[1]:>12}  {headers[2]:>10}  {headers[3]:>8}  {headers[4]:>12}")
    print("-" * 62)
    for r in rows:
        max_mem = r.get("max_memory_bytes")
        max_mem_str = f"{max_mem/1e9:.2f} GB" if isinstance(max_mem, (int, float)) and max_mem and max_mem > 0 else "-"
        print(
            f"{r.get('backend','-'):<10}  {r.get('latency_s',0.0):>12.4f}  {r.get('tokens_per_s',0.0):>10.2f}  {r.get('device','-'):>8}  {max_mem_str:>12}"
        )
    print()


def run_bench(args: argparse.Namespace) -> int:
    results = []
    try:
        for backend in args.backend:
            if backend == "hf":
                res = benchmark_hf(
                    model_id_or_path=args.target,
                    prompt=args.prompt,
                    max_new_tokens=args.max_new_tokens,
                    device=args.device,
                    trust_remote_code=args.trust_remote_code,
                    num_warmup=args.num_warmup,
                    num_runs=args.num_runs,
                )
                results.append(res)
            elif backend == "onnx":
                res = benchmark_onnx(
                    model_dir=args.target,
                    prompt=args.prompt,
                    max_new_tokens=args.max_new_tokens,
                    device=args.device,
                    num_warmup=args.num_warmup,
                    num_runs=args.num_runs,
                )
                results.append(res)
            elif backend == "gguf":
                gguf_path = args.target
                if os.path.isdir(gguf_path):
                    for name in os.listdir(gguf_path):
                        if name.endswith(".gguf"):
                            gguf_path = os.path.join(gguf_path, name)
                            break
                if not os.path.isfile(gguf_path):
                    raise FileNotFoundError(f"GGUF file not found: {args.target}")
                res = benchmark_gguf(
                    gguf_model_path=gguf_path,
                    prompt=args.prompt,
                    max_new_tokens=args.max_new_tokens,
                    llama_cli_path=args.llama_cli,
                    num_warmup=args.num_warmup,
                    num_runs=args.num_runs,
                )
                results.append(res)
    finally:
        _print_bench_results(results)
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    # Reduce noisy logs by default; allow opt-in via --verbose on any subcommand
    hf_logging.set_verbosity_error()
    
    # Suppress transformers progress bars globally
    try:
        from .quantize import _suppress_transformers_progress
        _suppress_transformers_progress()
        # Additional suppression
        import os
        os.environ["TRANSFORMERS_VERBOSITY"] = "error"
        os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
        os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    except Exception:
        pass
    # If user provided args without a subcommand, default to 'auto',
    # but do not hijack global flags like --help/-h/--version or when the first
    # token is itself a flag (e.g., `autopack --version`).
    tokens = sys.argv[1:] if argv is None else list(argv)
    if tokens and (tokens[0] not in {"quantize", "publish", "auto", "bench", "scan"}):
        is_global_help_or_version = any(t in {"-h", "--help", "--version"} for t in tokens)
        starts_with_flag = tokens[0].startswith("-")
        if not (is_global_help_or_version or starts_with_flag):
            tokens = ["auto", *tokens]

    # Parse arguments
    args = parse_args(tokens)

    # Derive default output directory from model if not provided
    def _derive_output_dir(model_id_or_path: str) -> str:
        # Use last path component for Hub IDs (user/model) or filesystem paths
        normalized = model_id_or_path.rstrip("/\\")
        name = os.path.basename(normalized)
        # Fallback: if basename is empty, use a generic name
        return name or "model"

    if getattr(args, "command", None) in {"auto", "quantize"}:
        if getattr(args, "output_dir", None) in (None, ""):
            default_out = _derive_output_dir(getattr(args, "model", getattr(args, "target", "model")))
            # For auto, keep variants under the derived folder directly
            setattr(args, "output_dir", default_out)
    # Normalize single-variant flag into variants list
    if getattr(args, "command", None) == "auto":
        if getattr(args, "hf_variant", None) and not getattr(args, "hf_variants", None):
            setattr(args, "hf_variants", [args.hf_variant])
    # Enable verbose warnings from Transformers when requested
    if getattr(args, "verbose", False):
        hf_logging.set_verbosity_warning()
    if args.command == "auto":
        return run_auto(args)
    if args.command == "quantize":
        return run_quantize(args)
    if args.command == "publish":
        return run_publish(args)
    if args.command == "bench":
        return run_bench(args)
    if args.command == "scan":
        report = scan_model(
            model_id_or_path=args.model,
            revision=args.revision,
            trust_remote_code=args.trust_remote_code,
            local_files_only=args.local_files_only,
            resolve_cache=args.resolve_cache,
        )
        print_scan_report(report, as_json=args.as_json, show_files=args.show_files, limit_files=args.limit_files)
        return 0
    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())


