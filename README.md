# TacitBridge — glasses to robot skill, through a local VLM

**Nebius x NVIDIA Global AI Hackathon 2026 / Physical AI track**

A person wears camera glasses and does a hands-on task. TacitBridge turns that
first-person stream into a robot-ready skill: the glasses capture the scene, a
local vision-language model on an edge tablet reads intent and steps, and an
action model maps the steps to robot motion. The tacit knowledge in a skilled
pair of hands becomes data a robot can replay.

```
glasses (first-person capture)
        -> edge tablet: local VLM (NVIDIA Nemotron) reads scene + intent
        -> action model (NVIDIA Isaac GR00T-class) emits robot motion
```

## Why it matters
Most robot-learning data is collected in a lab with instrumented rigs. Skilled
work happens in the field, on real benches, with ordinary hands. TacitBridge
collects there: the demonstrator just works, wearing glasses, and the pipeline
produces a structured skill trace (objects, grips, order, forces) ready for an
action model. No motion-capture suit, no teleoperation rig.

## What is in this repository
This repo is the **open demo client**: capture adapter, the Nemotron reasoning
wrapper, the skill-trace schema, and a viewer. It runs end to end against the
public Nemotron endpoint on Nebius Token Factory.

The production perception engine (the proprietary tacit-knowledge extractor and
decision gate) is **not** in this repo. The client talks to it over a documented
HTTP interface (`TACIT_ENGINE_URL`); a reference stub is included so the demo
runs without it. See [ARCHITECTURE.md](ARCHITECTURE.md).

## Quick start
```bash
pip install -r requirements.txt
export NEBIUS_API_KEY=...          # Nebius Token Factory
export TACIT_ENGINE_URL=stub       # use the bundled reference stub
python -m src.pipeline demo/sample_clip.mp4
```

## Demo
3-minute walkthrough: `demo/README.md`

## License
Apache 2.0. See [LICENSE](LICENSE).

Built by VIDRAFT (https://vidraft.net).
