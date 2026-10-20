# Alex Newton's AI rig

How I run my week on Claude: scheduled agents, custom plugins, a custom MCP server and a Python
data pipeline, mapped down to the implementation.

**▶ Interactive site: https://anewt225.github.io/ai-rig/**

| Tab | What it shows |
|---|---|
| Overview | The three workflows as cards, a week of scheduled runs, and what stays human. |
| Weekly rhythm | The agile loop: productivity sync and daily standup, time tracking, retro, week ahead; scorecard contract. |
| Career | Capture, tailoring, networking events, outreach, interviews, LinkedIn: Notion data model and scoring rubrics. |
| Personal | Finances check-in, state and federal tax assistant, home and health, travel; by method only. |
| Projects | Featured multi-unit franchise proposal (anonymized), then a gallery of side builds. |
| Platform | Stack, rules I build by, and data source reconciliation, with a table of contents. |

Each workflow opens with a clickable map; each phase is a collapsed card that opens to inputs, outputs, stack and process,: trigger, inputs, outputs, stack, and every step tagged code, model or me.

## Layout

```
src/index.html    the page (artifact-style body: no doctype/head)
build.py          wraps src/ into docs/index.html for GitHub Pages
docs/index.html   built page, served by Pages
archive/v0/       earlier site and deck versions
deck/             8-page written deck source (one HTML file per slide + deck.json); page 1 is an optional recipient cover note
```

Rebuild after editing `src/index.html`:

```bash
uv run --no-project python build.py
```

Numbers are as of 19 Oct 2026, taken from the system's own config files, run logs and repos.
Personal finance and household workflows are described by method only.
