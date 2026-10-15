# -*- coding: utf-8 -*-
"""End-to-end demo: capture -> engine extract -> Nemotron reason -> gate -> trace.

  python -m src.pipeline demo/sample_clip.mp4
  TACIT_ENGINE_URL=stub  uses the bundled reference stub.
"""
import json
import os
import sys

from .schema import Step, SkillTrace


def load_capture(path):
    """Normalize a source into (scene_text, events). Demo: read a sidecar .json
    next to the clip, or fall back to a built-in sample."""
    side = os.path.splitext(path)[0] + ".json"
    if os.path.exists(side):
        d = json.load(open(side, encoding="utf-8"))
        return d["scene"], d["events"]
    return (
        "A hand picks up a small screwdriver, seats the tip in a screw on a "
        "panel, turns it clockwise firmly, then sets the screwdriver down.",
        [
            {"action": "grasp", "target": "screwdriver", "grip": "pinch"},
            {"action": "seat", "target": "screw", "grip": "pinch"},
            {"action": "turn", "target": "screw", "grip": "pinch", "force": "firm"},
            {"action": "place", "target": "screwdriver", "grip": "none"},
        ],
    )


def call_engine(url, scene, events):
    if url == "stub":
        from . import engine_stub
        steps = engine_stub.extract(None, events)["steps"]
        return engine_stub.gate(steps)["accepted"]
    import urllib.request
    def post(ep, payload):
        req = urllib.request.Request(
            url + ep, data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"})
        return json.load(urllib.request.urlopen(req, timeout=120))
    steps = post("/extract", {"frames_ref": None, "events": events})["steps"]
    return post("/gate", {"steps": steps})["accepted"]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "demo/sample_clip.mp4"
    url = os.environ.get("TACIT_ENGINE_URL", "stub")
    scene, events = load_capture(path)

    accepted = call_engine(url, scene, events)

    # Nemotron refines the gated steps into the final trace when a key is set;
    # otherwise the gated steps are used directly so the demo still runs.
    if os.environ.get("NEBIUS_API_KEY"):
        from .nemotron import reason
        refined = reason(scene)
    else:
        refined = accepted

    trace = SkillTrace(task=scene[:60], source=os.path.basename(path))
    for i, s in enumerate(refined):
        trace.steps.append(Step(
            index=i, action=s.get("action", "move"), target=s.get("target", ""),
            grip=s.get("grip", "unknown"), force=s.get("force", "light"),
            note=s.get("note", "")))
    print(json.dumps(trace.to_dict(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
