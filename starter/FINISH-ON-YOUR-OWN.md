# Finish On Your Own

You made it through the workshop — or you're catching up later. This guide takes you from **sample data** to a **daily automated agent**.

Work through the steps in order. Each step is independently useful.

---

## Step 0: Confirm the starter works

```bash
cd workshop/starter
source .venv/bin/activate
ea-workshop --sample --dry-run
```

You should see a brief with Today's Focus, Work Plan, Wellness, Movement, and Tasks.

---

## Step 1: Make the prompt yours

**File:** `src/ea_workshop/synthesizer.py`

Edit `SYSTEM_PROMPT`. Try adding:

- Your tone ("warm but direct," "no corporate jargon")
- Hard caps ("max 5 tasks total," "never mention Slack")
- Sections you care about ("always include movement challenge")

**File:** `config.yaml`

Edit `prompt_rules` with life-specific rules:

```yaml
roles:
  - Work
  - Side Project
  - Personal

prompt_rules:
  - "I don't work weekends."
  - "Side Project is my newsletter — tag those emails."
  - "Max 2 urgent tasks per day."
```

Re-run after every change:

```bash
ea-workshop --sample --dry-run
```

---

## Step 2: Connect live Gmail + Calendar

### Google Cloud setup (~15 min)

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project (e.g. "ea-agent")
3. Enable **Gmail API** and **Google Calendar API**
4. **OAuth consent screen** → External → add your email as test user
5. **Credentials** → Create → OAuth client ID → **Desktop app**
6. Download JSON → save as `credentials/google_credentials.json`

### Authorize

```bash
python scripts/setup_google_auth.py
```

### Run live

```bash
ea-workshop --dry-run    # preview
ea-workshop              # writes output/Daily Brief — DATE.md
```

### Multi-account (advanced)

Copy the pattern from the full `daily-brief-agent` repo — one token file per Gmail account, loop collectors, tag each item with `account` label.

---

## Step 3: Add a task writer

The starter prints tasks at the bottom of the markdown brief. Next, push tasks to your todo app.

Pick **one**:

### Option A: Markdown only (simplest)

You're done. Copy tasks from the brief manually, or parse the `## Tasks` section.

### Option B: Todoist

1. Get API token from Todoist → Settings → Integrations
2. Create `src/ea_workshop/writers/todoist.py`:

```python
import os
import requests

def create_tasks(tasks: list) -> list[str]:
    token = os.environ["TODOIST_API_TOKEN"]
    created = []
    for task in tasks:
        resp = requests.post(
            "https://api.todoist.com/rest/v2/tasks",
            headers={"Authorization": f"Bearer {token}"},
            json={"content": task.title, "description": task.notes},
            timeout=30,
        )
        resp.raise_for_status()
        created.append(task.title)
    return created
```

3. Call it from `run.py` after `synthesize()`
4. Add `TODOIST_API_TOKEN` to `.env`

### Option C: Google Tasks

Use Google Tasks API with the same OAuth credentials. Add scope:
`https://www.googleapis.com/auth/tasks`

### Option D: Apple Reminders (macOS only)

```bash
pip install -e ".[apple]"
```

Copy `writers/reminders.py` and `reminder_dedupe.py` from the full `daily-brief-agent` repo. Grant Reminders permission to your Python binary in System Settings.

---

## Step 4: Dedupe (don't create the same task twice)

This is the #1 real-world bug. LLMs rephrase tasks daily.

**Minimum fix (prompt only):**

Pass your open tasks into the prompt — the starter already includes `existing_reminders` in sample data. For live runs, fetch open tasks from your todo app and populate `data.existing_reminders` before calling `synthesize()`.

**Better fix (code):**

Before creating any task:

1. Load ALL open tasks from your todo app
2. Skip if normalized title matches
3. Skip if fuzzy match (shared keywords)

See `daily-brief-agent/src/daily_brief/reminder_dedupe.py` for a full implementation.

---

## Step 5: Schedule daily runs

### Mac / Linux (cron)

```bash
crontab -e
```

```
0 7 * * * cd /full/path/to/workshop/starter && .venv/bin/ea-workshop >> ~/ea-brief.log 2>&1
```

### Mac (launchd — full build)

Copy `launchd/` and `scripts/install_launchd.sh` from `daily-brief-agent`.

### Windows (Task Scheduler)

1. Open Task Scheduler → Create Basic Task
2. Trigger: Daily, 7:00 AM
3. Action: Start a program
4. Program: `C:\path\to\starter\.venv\Scripts\python.exe`
5. Arguments: `-m ea_workshop.run`
6. Start in: `C:\path\to\starter`

### Cloud (GitHub Actions)

Run on a schedule in the cloud — good if your laptop isn't on at 7 AM. Requires storing API keys as GitHub secrets. Advanced; ask for a template if needed.

---

## Step 6: Weekend mode (optional)

Add to `run.py`:

```python
from datetime import datetime

if datetime.now().weekday() >= 5:  # Sat/Sun
    data.emails = [e for e in data.emails if e.account == "Personal"]
    data.calendar_events = [e for e in data.calendar_events if e.account == "Personal"]
    # use a different SYSTEM_PROMPT — see daily-brief-agent/src/daily_brief/weekend.py
```

Weekend prompt should say: personal life coach voice, no work tasks, life goals + wellness.

---

## Step 7: Upgrade to the full build

When you're ready for the complete experience:

| Feature | Full repo |
|---------|-----------|
| Apple Notes (collapsible sections) | `writers/notes.py` |
| Apple Reminders + dedupe | `writers/reminders.py` |
| 3 Gmail accounts | `collectors/google_mail.py` |
| Granola meeting notes | `collectors/granola.py` |
| Catch-up on wake | `launchd/` + `scheduler.py` |

Clone or copy patterns from `/Users/lindakinning/Projects/daily-brief-agent`.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ANTHROPIC_API_KEY not set` | `cp .env.example .env`, add key |
| Model 404 | Set `ANTHROPIC_MODEL=claude-sonnet-4-6` |
| Google OAuth browser doesn't open | Check `credentials/google_credentials.json` exists |
| Token expires every 7 days | Publish OAuth app to Production in Google Cloud |
| Brief too long | Tighten `SYSTEM_PROMPT` caps |
| All tasks marked urgent | Add rule: "max 2 today, most = this_week" |

---

## Share what you built

When your agent runs tomorrow morning, notice:

- Did you read the brief?
- Was Today's Focus actually right?
- Were tasks actionable or noise?

That's your feedback loop. Edit the prompt, not the code.

**The API keys are commodity. The prompts and rules are yours.**
