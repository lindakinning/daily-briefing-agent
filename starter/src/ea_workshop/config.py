from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


@dataclass
class AppConfig:
    raw: dict[str, Any]
    root: Path

    @classmethod
    def load(cls) -> AppConfig:
        root = project_root()
        load_dotenv(root / ".env")
        with (root / "config.yaml").open(encoding="utf-8") as handle:
            raw = yaml.safe_load(handle) or {}
        return cls(raw=raw, root=root)

    def path(self, *parts: str) -> Path:
        return self.root.joinpath(*parts)

    @property
    def anthropic_model(self) -> str:
        return os.environ.get(
            "ANTHROPIC_MODEL",
            self.raw.get("anthropic", {}).get("model", "claude-sonnet-4-6"),
        )

    def brief_output_dir(self) -> Path:
        rel = self.raw.get("outputs", {}).get("brief_dir", "output")
        return self.path(rel)
