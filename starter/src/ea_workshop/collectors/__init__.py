from __future__ import annotations

import json
from pathlib import Path

from ea_workshop.config import AppConfig
from ea_workshop.models import (
    CalendarEvent,
    CollectedData,
    EmailSummary,
    MeetingNote,
)


def load_sample_data(config: AppConfig) -> CollectedData:
    path = config.path("sample_data", "collected_data.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    return _parse_payload(payload)


def _parse_payload(payload: dict) -> CollectedData:
    data = CollectedData()
    data.collection_errors = list(payload.get("collection_errors", []))
    data.existing_reminders = list(payload.get("existing_reminders", []))

    for item in payload.get("emails", []):
        data.emails.append(EmailSummary(**item))

    for item in payload.get("calendar_events", []):
        data.calendar_events.append(CalendarEvent(**item))

    for item in payload.get("meeting_notes", []):
        data.meeting_notes.append(MeetingNote(**item))

    return data


def collect_live(config: AppConfig) -> CollectedData:
    """Collect from Google APIs. Requires OAuth setup — see FINISH-ON-YOUR-OWN.md."""
    from ea_workshop.collectors.google_live import collect_google_data

    return collect_google_data(config)
