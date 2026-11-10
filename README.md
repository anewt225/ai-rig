# Alex Newton's AI rig

How I run my week on Claude, Python and Notion, written up the way I would document a client's operating process: three workflows, each mapped down to its trigger, inputs, outputs, stack and steps, with every step marked as done by a script, by the model, or by me.

**▶ Interactive site: https://anewt225.github.io/ai-rig/**

The split the whole system follows: scripts do the arithmetic, the model does the judgment, and I make every decision that leaves my machine. Scheduled runs draft and propose. They never send.

## If you have five minutes

| Look at | Why |
|---|---|
| [Projects → the franchise proposal](https://anewt225.github.io/ai-rig/#projects) | A real February 2026 proposal for a four-store food-service franchise, client anonymized: Discover, Design and Deliver phases, each with a gate, and target outcomes stated as times (weekly KPI review, dashboard data age, daily production planning, manager training). It ends with what happened: the owner built his own version with AI, and what that says about where consulting value sits now. |
| [Weekly rhythm](https://anewt225.github.io/ai-rig/#rhythm) | An agile loop for one person: daily standup, time tracking, weekly retro, week-ahead plan. The scorecard counts a conversation only with evidence, and records unknown as null, not zero. |
| [Platform → Rules I build by](https://anewt225.github.io/ai-rig/#platform) | Eight rules, each tied to where it shows up in the system. Examples: numbers that must be right come from scripts before the model sees them; each kind of data has exactly one system of record; every run is safe to repeat and nothing is deleted. |
| Overview → What stays human | Planning, reflection, and every message, payment or filing. |

## What the site covers

| Tab | What it shows |
|---|---|
| Overview | The three workflows as cards, the system in five numbers, and what stays human. |
| Weekly rhythm | Productivity sync and daily standup, time tracking, weekly retro, week ahead and mid-week pulse; the scorecard contract. |
| Career | Capture, tailoring, applying, networking (events and individuals), interviews, LinkedIn; the Notion data model and the scoring rubrics. |
| Personal | Monthly finances check-in, state and federal tax filing assistant, home and health, travel. Described by method only. |
| Projects | The franchise proposal, then a gallery of side builds with links. |
| Platform | The stack in seven layers, the eight rules, and a data source reconciliation table: one owner per kind of data, and a rule for conflicts. |

Each workflow opens with a clickable map. Each phase is a collapsed card that opens to its inputs, outputs, stack and process.

## The system in numbers

As of 19 October 2026, taken from the system's own config files, run logs and repos:

- 32 connectors on my Claude account, plus 3 local MCP servers
- 4 plugins I wrote: 11 skills and 29 commands, versioned in git
- 25 tools in my custom TickTick MCP server (Python)
- 7 scheduled jobs: 3 Claude routines and 4 Windows tasks
- 127 agent-written reports on file: standups, briefs, retros, plans

The plugins and the MCP server live in a private repo. A shareable rebuild of the job-search plugin is public: [job-search-assistant](https://github.com/anewt225/job-search-assistant).

## What is not here

Personal finance, tax and health workflows are described by method only: no institution names, account numbers or figures. The client in the franchise proposal is anonymized. This repo holds the write-up, not the automation code.

## Repo layout

```
src/index.html    the page (artifact-style body: no doctype or head)
build.py          wraps src/index.html into docs/index.html for GitHub Pages
docs/index.html   built page, served by Pages
deck/             8-page written deck (one HTML file per slide + deck.json); page 1 is an optional cover note for one recipient
archive/v0/       earlier site and deck versions
```

The page is a single self-contained HTML file with no framework and no dependencies. `build.py` uses only the Python standard library.

Rebuild after editing `src/index.html`:

```bash
uv run --no-project python build.py
```

Without `uv`, `python build.py` does the same thing.

---

Built by [Alex Newton](https://www.linkedin.com/in/anewt) with Claude Code.
