# -*- coding: utf-8 -*-
"""Reference stub for the private tacit-knowledge engine.

Set TACIT_ENGINE_URL=stub to use this. It returns the same shapes the
production engine does, so the demo runs end to end without the real service.
The real extractor and decision gate are proprietary and not shipped here.
"""


def extract(frames_ref, events):
    """Turn raw capture into candidate steps. Deterministic placeholder."""
    steps = []
    for i, ev in enumerate(events):
        steps.append({
            "index": i,
            "action": ev.get("action", "move"),
            "target": ev.get("target", "object"),
            "grip": ev.get("grip", "unknown"),
            "force": ev.get("force", "light"),
            "note": ev.get("note", ""),
        })
    return {"steps": steps}


def gate(steps):
    """Accept steps that have a named target. Placeholder for the real gate."""
    accepted = [s for s in steps if s.get("target") and s["target"] != "object"]
    return {"accepted": accepted}
