# Alex Newton's AI rig

How I run my week on Claude: scheduled agents, custom plugins, a custom MCP server and a Python
data pipeline, mapped down to the implementation.

**▶ Interactive site: https://anewt225.github.io/ai-rig/**

| Tab | What it shows |
|---|---|
| Overview | The three workflows as cards, a week of scheduled runs, and what stays human. |
| Weekly rhythm | Standup, morning brief, time tracking, retro and sprint planning: flow, spec cards, scorecard contract. |
| Career | Capture, tailoring, outreach, interviews, LinkedIn and /today: Notion data model and the four scoring rubrics. |
| Money & home | The reconciled-ledger pipeline, filing assistant and household loops, by method only. |
| Platform | Stack, systems of record, rules I build by, side projects, and a client design sketch. |

Each workflow piece opens to a spec card: trigger, inputs, outputs, stack, and every step tagged code, model or me.

## Layout

```
src/index.html    the page (artifact-style body: no doctype/head)
build.py          wraps src/ into docs/index.html for GitHub Pages
docs/index.html   built page, served by Pages
deck/             7-page written deck source (one HTML file per slide + deck.json); page 1 is an optional recipient cover note
```

Rebuild after editing `src/index.html`:

```bash
uv run --no-project python build.py
```

Numbers are as of 19 Oct 2026, taken from the system's own config files, run logs and repos.
Personal finance and household workflows are described by method only.
