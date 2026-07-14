from __future__ import annotations

import json
import logging
import os
import re
from typing import Any

import anthropic

from ea_workshop.config import AppConfig
from ea_workshop.models import (
    BriefSections,
    CollectedData,
    FocusItem,
    MovementItem,
    SynthesisResult,
    TaskItem,
)

logger = logging.getLogger(__name__)

# ── WORKSHOP: Edit this prompt to make the agent yours ──────────────────

SYSTEM_PROMPT = """You are an exceptional executive assistant preparing a focused morning daily brief.

Your voice is warm, clear, and concise — like a trusted EA who protects the client's attention.

The brief must be SHORT and scannable. Synthesize; never dump raw lists.

Produce:
1. A tight daily brief (integrated day, role-tagged)
2. A separate task list for the user's todo app

Critical brief rules:
- focus_today: MAX 3 items only
- work_plan: ONE short narrative paragraph with time blocks and total effort estimate
- email_actions_by_role: max 2 bullets per role
- meeting_followups_by_role: max 2 bullets per role
- planning_ahead: max 2 bullets
- time_savers: max 2 bullets
- wellness: 2-3 practical nudges
- movement_challenge: 3-5 micro-movements (≤30 min each)

Task rules:
- urgency: critical | today | this_week | whenever
- At most 2 tasks may be critical or today
- Include time_estimate for each task
- Only explicit or strongly implied action items
- NEVER duplicate items in existing_reminders

Respond with valid JSON only, no markdown fences."""


def _existing_reminders_block(data: CollectedData) -> str:
    if not data.existing_reminders:
        return "No open reminders on file."
    return "\n".join(
        f"- [{r.get('role', '?')}] {r.get('title', '')}" for r in data.existing_reminders
    )


def _build_user_prompt(config: AppConfig, data: CollectedData) -> str:
    roles = ", ".join(config.raw.get("roles", ["Work", "Personal"]))
    rules = "\n".join(f"- {r}" for r in config.raw.get("prompt_rules", []))
    context = json.dumps(data.to_context_dict(), indent=2, default=str)

    return f"""Prepare today's executive assistant brief.

Roles: {roles}

Open reminders already tracked (do NOT duplicate as new tasks):
{_existing_reminders_block(data)}

Additional rules:
{rules}

Data:
{context}

Respond with this JSON structure:
{{
  "brief_sections": {{
    "greeting": "Warm 1 sentence",
    "day_overview": "1-2 sentences",
    "integrated_schedule": [
      {{"time": "9:00 AM", "role": "Work", "title": "Event", "detail": ""}}
    ],
    "focus_today": [
      {{"role": "Work", "item": "Biggest thing", "why": "Why today"}}
    ],
    "work_plan": "One paragraph with time blocks...",
    "email_actions_by_role": {{"Work": [], "Personal": []}},
    "meeting_followups_by_role": {{"Work": [], "Personal": []}},
    "planning_ahead": [],
    "time_savers": [],
    "wellness": [],
    "movement_challenge": [
      {{"activity": "10-min walk", "duration": "10 min", "when": "after lunch"}}
    ]
  }},
  "tasks": [
    {{
      "title": "Verb-first task",
      "role": "Work",
      "urgency": "this_week",
      "time_estimate": "20 min",
      "notes": "Source context",
      "due_date": null,
      "source": "email"
    }}
  ]
}}"""


def _extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        text = match.group(1).strip()
    return json.loads(text)


def _parse_result(payload: dict[str, Any]) -> SynthesisResult:
    raw = payload.get("brief_sections", {})

    focus = [
        FocusItem(
            role=str(item.get("role", "Work")),
            item=str(item.get("item", "")),
            why=str(item.get("why", "")),
        )
        for item in raw.get("focus_today", [])[:3]
        if item.get("item")
    ]

    movement = []
    for item in raw.get("movement_challenge", [])[:5]:
        if isinstance(item, dict) and item.get("activity"):
            movement.append(
                MovementItem(
                    activity=str(item["activity"]),
                    duration=str(item.get("duration", "")),
                    when=str(item.get("when", "")),
                )
            )

    sections = BriefSections(
        greeting=str(raw.get("greeting", "")),
        day_overview=str(raw.get("day_overview", "")),
        focus_today=focus,
        work_plan=str(raw.get("work_plan", "")),
        integrated_schedule=list(raw.get("integrated_schedule", [])),
        wellness=[str(v) for v in raw.get("wellness", []) if v],
        movement_challenge=movement,
        email_actions_by_role={
            str(k): [str(v) for v in vals if v]
            for k, vals in raw.get("email_actions_by_role", {}).items()
            if isinstance(vals, list)
        },
        meeting_followups_by_role={
            str(k): [str(v) for v in vals if v]
            for k, vals in raw.get("meeting_followups_by_role", {}).items()
            if isinstance(vals, list)
        },
        planning_ahead=[str(v) for v in raw.get("planning_ahead", []) if v],
        time_savers=[str(v) for v in raw.get("time_savers", []) if v],
    )

    tasks = []
    for item in payload.get("tasks", []):
        title = str(item.get("title", "")).strip()
        if not title:
            continue
        due = item.get("due_date")
        if due in (None, "null", ""):
            due = None
        tasks.append(
            TaskItem(
                title=title,
                role=str(item.get("role", "Work")),
                urgency=str(item.get("urgency", "this_week")),
                time_estimate=str(item.get("time_estimate", "")),
                notes=str(item.get("notes", "")),
                due_date=due,
                source=str(item.get("source", "")),
            )
        )

    return SynthesisResult(brief_sections=sections, tasks=tasks)


def synthesize(config: AppConfig, data: CollectedData) -> SynthesisResult:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key."
        )

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=config.anthropic_model,
        max_tokens=config.raw.get("anthropic", {}).get("max_tokens", 4096),
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _build_user_prompt(config, data)}],
    )

    text = "".join(block.text for block in message.content if hasattr(block, "text"))
    result = _parse_result(_extract_json(text))
    logger.info("Synthesized brief with %d tasks", len(result.tasks))
    return result
