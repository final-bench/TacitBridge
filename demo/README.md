# Demo video plan (under 3 minutes)

Target: judges see glasses -> local VLM -> robot skill trace, running, in one take.

| time | shot | what is shown |
|------|------|---------------|
| 0:00-0:20 | hook | A person in camera glasses does a short bench task (seat and turn a screw). Caption: "Skilled hands. No rig." |
| 0:20-0:50 | problem | One line: robot-learning data is collected in labs, not in the field. We collect in the field. |
| 0:50-1:40 | pipeline live | Screen capture of `python -m src.pipeline` on the tablet. Show the glasses clip going in and the JSON skill trace coming out, step by step. Point out Nemotron doing the reasoning on the edge. |
| 1:40-2:20 | act | The skill trace drives a robot arm (or a simulated GR00T-class arm) repeating the screw task. |
| 2:20-2:50 | why it matters | Field data, any task, any pair of hands. Scale robot skills without rigs. |
| 2:50-3:00 | close | VIDRAFT logo, repo URL, Apache 2.0. |

## Needed from 14팀 (VIGLASS)
- 30-60s first-person clip of a clean bench task, glasses POV
- One real or simulated robot-arm replay of the same task

## Shot rules (self-review 5 before sending)
1. No proprietary engine internals, no model names beyond Nemotron/NVIDIA, on screen
2. No VIDRAFT confidential UI, no GPU counts, no Rebellions/NPU mention
3. Audio clear, captions burned in, English
4. Under 3:00, 1080p, public link works in incognito
5. Repo URL on screen resolves to the public Apache-2.0 repo
