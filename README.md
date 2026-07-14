# EA Workshop Starter

Build your own **Executive Assistant morning agent** in 75 minutes — or finish at your own pace.

## Workshop quick start (5 min, no Google)

```bash
cd workshop/starter
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
# Edit .env — add your ANTHROPIC_API_KEY

ea-workshop --sample              # writes output/Daily Brief — YYYY-MM-DD.md
ea-workshop --sample --dry-run    # preview in terminal
```

## What this repo includes

| Piece | File | Workshop activity |
|-------|------|-------------------|
| Sample data | `sample_data/collected_data.json` | Run immediately |
| Prompts | `src/ea_workshop/synthesizer.py` | **Live edit together** |
| Your rules | `config.yaml` → `prompt_rules` | **Live edit together** |
| Brief writer | `src/ea_workshop/writers/markdown.py` | Works on all platforms |
| Live collectors | `src/ea_workshop/collectors/google_live.py` | Homework / stretch |
| Finish guide | `FINISH-ON-YOUR-OWN.md` | After the session |

## Live coding path (during workshop)

1. `ea-workshop --sample --dry-run` — see output
2. Edit `SYSTEM_PROMPT` in `synthesizer.py` — re-run
3. Add a `prompt_rule` in `config.yaml` — re-run
4. Open `writers/markdown.py` — tweak brief format
5. (Stretch) Add API key and run without `--sample`

## Commands

```bash
ea-workshop --sample           # sample inbox + calendar
ea-workshop --sample --dry-run # print only
ea-workshop                    # live Google data (needs OAuth)
ea-workshop --dry-run          # live data, print only
python scripts/setup_google_auth.py   # one-time Google login
```

## Project structure

```
starter/
├── config.yaml              ← your roles + rules
├── sample_data/             ← fake inbox for workshop
├── output/                  ← daily briefs land here
├── credentials/             ← google_credentials.json (you add)
├── src/ea_workshop/
│   ├── synthesizer.py       ← THE PROMPT (edit this)
│   ├── writers/markdown.py  ← brief output
│   ├── collectors/          ← data sources
│   └── run.py               ← entry point
├── FINISH-ON-YOUR-OWN.md    ← complete the build later
└── scripts/setup_google_auth.py
```

## Full reference build

The parent repo (`daily-brief-agent`) adds:

- Apple Notes with collapsible sections + checkboxes
- Apple Reminders with dedupe + urgency tiers
- Multi-account Gmail, Granola meeting notes
- Weekend personal mode
- 7 AM scheduling with catch-up on wake

## Need help?

Read `FINISH-ON-YOUR-OWN.md` and `../participant-handout.md`.
