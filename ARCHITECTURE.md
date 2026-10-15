# Architecture and the public/private boundary

## Three stages
1. **Capture (glasses).** First-person video plus hand and audio cues. The
   capture adapter normalizes any source into frames plus a short event track.
2. **Reason (edge tablet, local VLM).** NVIDIA Nemotron reads each segment and
   produces a step list: objects, grips, order, and rough forces. This is the
   part the hackathon stack exercises directly.
3. **Act (action model).** The step list is lowered to an action schema an
   Isaac GR00T-class model consumes to produce robot motion.

## What is open in this repo
- Capture adapter and frame/event normalizer
- Nemotron reasoning wrapper (prompts, schema, retry, cost guard)
- Skill-trace schema (`src/schema.py`) and viewer
- Reference engine **stub** so the demo runs with no private service

## What stays private (behind TACIT_ENGINE_URL)
- The tacit-knowledge extractor (how raw first-person motion becomes a clean,
  de-noised skill trace)
- The decision gate that scores and accepts a step before it is emitted
- Any model weights or checkpoints

The client never ships these. It calls a documented HTTP interface:

```
POST {TACIT_ENGINE_URL}/extract   body: {frames_ref, events}  -> {steps[]}
POST {TACIT_ENGINE_URL}/gate      body: {steps}               -> {accepted[]}
```

Set `TACIT_ENGINE_URL=stub` to use the bundled deterministic stub, which is
good enough to demonstrate the full flow and to let judges run the repo. The
production engine is a drop-in replacement that returns the same shapes.

## Why this split is honest, not evasive
The demo is fully runnable and open under Apache 2.0. The judged artifact (the
pipeline, schema, and Nemotron integration) is all here. What we keep private is
our pre-existing commercial engine, which is not what the hackathon asks us to
build. This mirrors how a real product open-sources its SDK while keeping its
service proprietary.
