# -*- coding: utf-8 -*-
"""Skill-trace schema: the structured output a robot action model consumes."""
from dataclasses import dataclass, field, asdict
from typing import List


@dataclass
class Step:
    index: int
    action: str            # e.g. "grasp", "place", "turn", "press"
    target: str            # object acted on
    grip: str = "unknown"  # e.g. "pinch", "power", "none"
    force: str = "light"   # "light" | "firm" | "hard"
    note: str = ""


@dataclass
class SkillTrace:
    task: str
    source: str
    steps: List[Step] = field(default_factory=list)

    def to_dict(self):
        d = asdict(self)
        return d
