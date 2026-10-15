# -*- coding: utf-8 -*-
"""Nemotron reasoning wrapper on Nebius Token Factory.

Reads a segment description and returns a step list in the skill-trace shape.
"""
import json
import os
import urllib.request

BASE = os.environ.get("NEBIUS_BASE", "https://api.studio.nebius.com/v1")
MODEL = os.environ.get("NEMOTRON_MODEL", "nvidia/Llama-3_3-Nemotron-Super-49B-v1")

PROMPT = (
    "You read a first-person work clip described as scene text and return the "
    "hand steps a robot would replay. Output strict JSON: a list of objects "
    "with keys index, action, target, grip, force, note. Actions are short "
    "verbs (grasp, place, turn, press, pour). grip is pinch|power|none. "
    "force is light|firm|hard. No prose, JSON only.\n\nScene:\n"
)


def reason(scene_text):
    key = os.environ.get("NEBIUS_API_KEY", "")
    if not key:
        raise SystemExit("set NEBIUS_API_KEY")
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": PROMPT + scene_text}],
        "temperature": 0.2,
        "max_tokens": 1200,
    }).encode()
    req = urllib.request.Request(
        BASE + "/chat/completions", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    out = json.load(urllib.request.urlopen(req, timeout=120))
    txt = out["choices"][0]["message"]["content"].strip()
    if txt.startswith("```"):
        txt = txt.split("```")[1].lstrip("json").strip()
    return json.loads(txt)
