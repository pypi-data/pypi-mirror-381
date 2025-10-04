import json
import os
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional


@dataclass
class StepRecord:
    id: str
    status: str  # pending|running|completed|failed|skipped
    started_at: Optional[float] = None
    finished_at: Optional[float] = None
    message: Optional[str] = None
    output_path: Optional[str] = None


class PipelineState:
    """
    Simple JSON-backed pipeline state for resume/force-step.
    Stored at `<output_dir>/.autopack_state.json` by default.
    """

    def __init__(self, state_path: str):
        self.state_path = state_path
        self.meta: Dict[str, str] = {}
        self.steps: Dict[str, StepRecord] = {}
        self._loaded: bool = False

    @staticmethod
    def default_path(output_dir: str) -> str:
        return os.path.join(output_dir, ".autopack_state.json")

    def load(self) -> None:
        if self._loaded:
            return
        try:
            with open(self.state_path, "r") as f:
                data = json.load(f)
            self.meta = dict(data.get("meta", {}))
            steps = data.get("steps", {}) or {}
            for k, v in steps.items():
                self.steps[k] = StepRecord(
                    id=v.get("id", k),
                    status=v.get("status", "pending"),
                    started_at=v.get("started_at"),
                    finished_at=v.get("finished_at"),
                    message=v.get("message"),
                    output_path=v.get("output_path"),
                )
        except FileNotFoundError:
            self.meta = {}
            self.steps = {}
        self._loaded = True

    def save(self) -> None:
        os.makedirs(os.path.dirname(self.state_path) or ".", exist_ok=True)
        data = {
            "meta": self.meta,
            "steps": {k: asdict(v) for k, v in self.steps.items()},
        }
        tmp = self.state_path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, self.state_path)

    def set_meta(self, key: str, value: str) -> None:
        self.meta[key] = value
        self.save()

    def init_steps(self, step_ids: List[str]) -> None:
        self.load()
        for sid in step_ids:
            if sid not in self.steps:
                self.steps[sid] = StepRecord(id=sid, status="pending")
        # Remove orphan steps that are no longer planned
        to_del = [sid for sid in self.steps.keys() if sid not in step_ids]
        for sid in to_del:
            del self.steps[sid]
        self.save()

    def is_completed(self, step_id: str) -> bool:
        self.load()
        rec = self.steps.get(step_id)
        return bool(rec and rec.status == "completed")

    def mark_running(self, step_id: str, message: Optional[str] = None) -> None:
        self.load()
        rec = self.steps.get(step_id) or StepRecord(id=step_id, status="pending")
        rec.status = "running"
        rec.started_at = time.time()
        rec.message = message
        self.steps[step_id] = rec
        self.save()

    def mark_completed(self, step_id: str, output_path: Optional[str] = None, message: Optional[str] = None) -> None:
        self.load()
        rec = self.steps.get(step_id) or StepRecord(id=step_id, status="pending")
        rec.status = "completed"
        if rec.started_at is None:
            rec.started_at = time.time()
        rec.finished_at = time.time()
        rec.output_path = output_path or rec.output_path
        rec.message = message or rec.message
        self.steps[step_id] = rec
        self.save()

    def mark_failed(self, step_id: str, message: Optional[str] = None) -> None:
        self.load()
        rec = self.steps.get(step_id) or StepRecord(id=step_id, status="pending")
        rec.status = "failed"
        if rec.started_at is None:
            rec.started_at = time.time()
        rec.finished_at = time.time()
        rec.message = message
        self.steps[step_id] = rec
        self.save()

    def mark_skipped(self, step_id: str, message: Optional[str] = None) -> None:
        self.load()
        rec = self.steps.get(step_id) or StepRecord(id=step_id, status="pending")
        rec.status = "skipped"
        rec.finished_at = time.time()
        rec.message = message
        self.steps[step_id] = rec
        self.save()


