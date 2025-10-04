# Changelog

## [0.1.5.0] - 2025-10-03

### Added
- Planning and resume support:
  - `--plan` prints a dry-run plan with estimates for downloads, RAM/VRAM, temp disk, and time per step for `auto` and `quantize`.
  - `--resume` resumes partially completed runs using a new JSON pipeline state at `<output_dir>/.autopack_state.json`.
  - `--force-step` allows forcing specific steps to re-run (e.g., `hf:bnb-4bit`, `onnx`, `gguf:Q4_K_M`).
- New module `autopack/state.py` implementing a simple JSON-backed state manager with step statuses.

### Changed
- `auto` and `quantize` now initialize a step plan and mark step-level statuses (`pending`, `running`, `completed`, `failed`, `skipped`).
- README updated with a "Planning and Resume" section and CLI flag references.

[0.1.5.0]: https://github.com/GranulaVision/autopack/releases/tag/v0.1.5.0

## [0.1.4.1] - 2025-09-15

### Added
- New `scan` subcommand to inspect models or local folders and print:
  - Config summary (arch, layers, heads, context length, RoPE scaling)
  - Tokenizer info and chat template presence
  - Export support hints (HF/ONNX/GGUF suitability)
  - Suggestions for next commands
- Enhanced scan report details:
  - Human-readable sizes and accurate weight/total bytes (local and remote)
  - File summary: total files, `config.json` presence, tokenizer files present/missing
  - Weight file counts (safetensors vs other)
  - Top-5 largest files by size

### Fixed
- Correct size reporting for remote models using Hub metadata with `files_metadata=True`.

[0.1.4.1]: https://github.com/GranulaVision/autopack/releases/tag/v0.1.4.1

## [0.1.4.0] - 2025-09-12

### Changed
- BitsAndBytes 4-bit defaults: prefer FP16 compute on CUDA (BF16 otherwise), disable double quantization to reduce per-token overhead while retaining `nf4` quant type.
- BitsAndBytes 8-bit defaults: explicitly disable FP32 CPU offload and set `llm_int8_threshold=6.0` to avoid slow fallbacks.

### Notes
- These changes target more stable throughput and prevent accidental CPU offload. Quantization primarily reduces memory usage; FP16/BF16 can still be faster for batch=1 autoregressive generation on many GPUs.

[0.1.4.0]: https://github.com/GranulaVision/autopack/releases/tag/v0.1.4.0

## [0.1.3.2] - 2025-09-10

### Added
- `--hf-variant` flag for single-variant runs (convenience alias for `--hf-variants <one>`).
- `--hf-variants` flag to limit which HF variants to produce in `auto`.
- Auto-detection of pre-quantized models (e.g., MxFP4) to skip conflicting BitsAndBytes variants.
- Model resolution to local cache once to avoid repeated downloads for large models.
- Memory cleanup between variants to free RAM/VRAM after each save.

### Changed
- `auto` now resolves the model to a local snapshot and reuses it for all variants.
- Pre-quantized models automatically skip bnb-4bit and bnb-8bit variants to avoid conflicts.

### Fixed
- Prevent quantization config conflicts when loading pre-quantized models.

[0.1.3.2]: https://github.com/GranulaVision/autopack/releases/tag/v0.1.3.2

## [0.1.3.1] - 2025-09-10

### Added
- Benchmarking is enabled by default for `auto`; new `--no-bench` flag to disable.
- Default subcommand: running `autopack <model>` now implies `auto`.
- Default output directory: if `-o/--output-dir` is omitted for `auto`/`quantize`, it uses the last segment of the model id/path (e.g., `user/model` -> `model`).

### Changed
- Tuned default benchmark settings for fast runs (max_new_tokens=16, warmup=0, runs=1).
- CLI help/version handling no longer gets hijacked by default-to-auto logic.
- README updated to highlight simplified CLI defaults and default benchmarking.

### Fixed
- Replaced heuristic speedup table in `auto` with real Tokens/s and speedup vs bf16 by default.
- Prevent conflict when loading pre-quantized models (e.g., MxFP4): skip passing BitsAndBytes config if a non-BNB quantization is detected in config.

[0.1.3.1]: https://github.com/GranulaVision/autopack/releases/tag/v0.1.3.1

All notable changes to this project will be documented in this file.

## [0.1.3] - 2025-09-09

### Added
- CLI flags: `--skip-existing`, `--summary-json`, and `--eval-text-key`.
- Machine-readable `summary.json` generation alongside the auto README.

### Changed
- Generated README usage now recommends `accelerate` and `safetensors` and uses `AutoModelForCausalLM`.
- Perplexity evaluation runs with `model.eval()` and `torch.inference_mode()`; text column is configurable.
- Quantization ensures `model.eval()` before save and sets `pad_token` if missing.

### Removed
- `ggml` output option from CLI; GGML export is not supported in this version.

### Fixed
- GGUF exporter now cleans temporary Hub snapshots and supports Windows virtualenv paths.
- Version synchronized between package and project metadata (`0.1.3`).

[0.1.3]: https://github.com/GranulaVision/autopack/releases/tag/v0.1.3

