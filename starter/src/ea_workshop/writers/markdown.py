from __future__ import annotations

from datetime import date
from pathlib import Path

from ea_workshop.config import AppConfig
from ea_workshop.models import BriefSections, SynthesisResult, TaskItem


def _format_brief_markdown(sections: BriefSections, tasks: list[TaskItem]) -> str:
    lines = [
        f"# Daily Brief — {date.today().strftime('%A, %B %d, %Y')}",
        "",
        sections.greeting,
        "",
        sections.day_overview,
        "",
        "## Today's Focus",
    ]
    for item in sections.focus_today:
        why = f" — *{item.why}*" if item.why else ""
        lines.append(f"- [ ] **[{item.role}]** {item.item}{why}")

    if sections.work_plan:
        lines.extend(["", "## Work Plan", "", sections.work_plan])

    if sections.integrated_schedule:
        lines.extend(["", "## Your Day"])
        for event in sections.integrated_schedule:
            time = event.get("time", "")
            role = event.get("role", "")
            title = event.get("title", "")
            detail = event.get("detail", "")
            suffix = f" — {detail}" if detail else ""
            lines.append(f"- **{time}** [{role}] {title}{suffix}")

    for role, items in sections.email_actions_by_role.items():
        if items:
            lines.extend(["", f"## Email Actions — {role}"])
            for item in items:
                lines.append(f"- [ ] {item}")

    for role, items in sections.meeting_followups_by_role.items():
        if items:
            lines.extend(["", f"## Meeting Follow-ups — {role}"])
            for item in items:
                lines.append(f"- [ ] {item}")

    if sections.wellness:
        lines.extend(["", "## Wellness"])
        for item in sections.wellness:
            lines.append(f"- {item}")

    if sections.movement_challenge:
        lines.extend(["", "## Movement Challenge"])
        for item in sections.movement_challenge:
            meta = ", ".join(x for x in [item.duration, item.when] if x)
            suffix = f" *({meta})*" if meta else ""
            lines.append(f"- [ ] {item.activity}{suffix}")

    if tasks:
        lines.extend(["", "## Tasks for your todo app", ""])
        for task in tasks:
            meta = []
            if task.time_estimate:
                meta.append(f"~{task.time_estimate}")
            if task.urgency:
                meta.append(task.urgency)
            suffix = f" ({', '.join(meta)})" if meta else ""
            lines.append(f"- [ ] **[{task.role}]** {task.title}{suffix}")

    return "\n".join(lines) + "\n"


def write_markdown_brief(
    config: AppConfig,
    result: SynthesisResult,
    *,
    dry_run: bool = False,
) -> Path:
    content = _format_brief_markdown(result.brief_sections, result.tasks)
    prefix = config.raw.get("outputs", {}).get("brief_prefix", "Daily Brief")
    filename = f"{prefix} — {date.today().isoformat()}.md"
    path = config.brief_output_dir() / filename

    if dry_run:
        print(content)
        return path

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


# ── STRETCH GOAL: Add writers/todoist.py or writers/google_tasks.py ─────
# See FINISH-ON-YOUR-OWN.md
