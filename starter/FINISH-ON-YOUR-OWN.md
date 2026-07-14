# Finish On Your Own

You made it through the workshop — or you're catching up later. This guide takes you from **sample data** to a **daily automated agent**.

Work through the steps in order. Each step is independently useful.

---

## Step 0: Confirm the starter works

```bash
cd starter
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

There's no bundled code for this — here's the shape of it: store one OAuth token file per Gmail account (e.g. `credentials/token_work.json`, `credentials/token_personal.json`), loop `collect_google_data()` once per token, and set the `account` field on each `EmailSummary`/`CalendarEvent` as you go so the prompt can tell them apart.

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

There's no bundled writer for this yet — you'll write `src/ea_workshop/writers/reminders.py` using the `pyobjc-framework-EventKit` package (already installed above). At a high level: request calendar/reminders access via `EventKit.EKEventStore`, create an `EKReminder` per task, and set its list, title, and notes. The first run will prompt for permission — approve it in **System Settings → Privacy & Security → Reminders**.

---

## Step 4: Dedupe (don't create the same task twice)

This is the #1 real-world bug. LLMs rephrase tasks daily.

**Minimum fix (prompt only):**

Pass your open tasks into the prompt — the starter already includes `existing_reminders` in sample data. For live runs, fetch open tasks from your todo app and populate `data.existing_reminders` before calling `synthesize()`.

**Better fix (code):**

Before creating any task:

1. Load ALL open tasks from your todo app
2. Skip if normalized title matches (lowercase, strip punctuation, compare)
3. Skip if fuzzy match — Python's built-in `difflib.SequenceMatcher(None, a, b).ratio()` above ~0.75 is a reasonable starting threshold for "probably the same task"

---

## Step 5: Schedule daily runs

### Mac / Linux (cron)

```bash
crontab -e
```

```
0 7 * * * cd /full/path/to/starter && .venv/bin/ea-workshop >> ~/ea-brief.log 2>&1
```

### Mac (launchd — runs even if you missed 7 AM)

launchd catches up on wake, where cron just skips the missed run. Save this as `~/Library/LaunchAgents/com.eaworkshop.daily.plist` (swap in your real paths):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.eaworkshop.daily</string>
  <key>ProgramArguments</key>
  <array>
    <string>/full/path/to/starter/.venv/bin/ea-workshop</string>
  </array>
  <key>WorkingDirectory</key><string>/full/path/to/starter</string>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>7</integer><key>Minute</key><integer>0</integer></dict>
  <key>RunAtLoad</key><false/>
  <key>StandardOutPath</key><string>/tmp/ea-brief.log</string>
  <key>StandardErrorPath</key><string>/tmp/ea-brief-error.log</string>
</dict>
</plist>
```

Then load it: `launchctl load ~/Library/LaunchAgents/com.eaworkshop.daily.plist`

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
    # swap in a second system prompt for weekends — copy SYSTEM_PROMPT in
    # synthesizer.py, rename it WEEKEND_PROMPT, and pass it to synthesize()
    # based on the day of week
```

Weekend prompt should say: personal life coach voice, no work tasks, life goals + wellness.

---

## Step 7: Where to take it from here

Everything above is the complete build — there's no separate "full" repo waiting behind it. Once you've worked through Steps 1–6 you have all the pieces; from here it's a matter of which of these you want to add next:

| Feature | Where it lives | Covered above |
|---------|-----------------|-----------------|
| A second task writer (Todoist / Google Tasks / Apple Reminders) | new file under `writers/` | Step 3 |
| Dedupe so tasks don't repeat daily | inside your chosen writer, before creating | Step 4 |
| Scheduled daily runs | cron, launchd, or Task Scheduler | Step 5 |
| Weekend mode | a few lines in `run.py` + a second prompt | Step 6 |
| Multiple Gmail accounts | loop the collector, tag by account | Step 2 |

If you build something worth reusing across cohorts, that's the point where a second, shared repo starts to make sense — but you don't need one to have a complete, working agent.

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
