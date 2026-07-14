from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EmailSummary:
    id: str
    subject: str
    sender: str
    snippet: str
    date: str
    is_unread: bool
    is_starred: bool
    account: str = "Work"


@dataclass
class CalendarEvent:
    id: str
    title: str
    start: str
    end: str
    location: str = ""
    account: str = "Work"


@dataclass
class MeetingNote:
    id: str
    title: str
    date: str
    summary: str = ""
    attendees: list[str] = field(default_factory=list)


@dataclass
class FocusItem:
    role: str
    item: str
    why: str = ""


@dataclass
class MovementItem:
    activity: str
    duration: str = ""
    when: str = ""


@dataclass
class TaskItem:
    title: str
    role: str = "Work"
    urgency: str = "this_week"
    time_estimate: str = ""
    notes: str = ""
    due_date: str | None = None
    source: str = ""


@dataclass
class BriefSections:
    greeting: str = ""
    day_overview: str = ""
    focus_today: list[FocusItem] = field(default_factory=list)
    work_plan: str = ""
    integrated_schedule: list[dict[str, str]] = field(default_factory=list)
    wellness: list[str] = field(default_factory=list)
    movement_challenge: list[MovementItem] = field(default_factory=list)
    email_actions_by_role: dict[str, list[str]] = field(default_factory=dict)
    meeting_followups_by_role: dict[str, list[str]] = field(default_factory=dict)
    planning_ahead: list[str] = field(default_factory=list)
    time_savers: list[str] = field(default_factory=list)


@dataclass
class SynthesisResult:
    brief_sections: BriefSections
    tasks: list[TaskItem]


@dataclass
class CollectedData:
    emails: list[EmailSummary] = field(default_factory=list)
    calendar_events: list[CalendarEvent] = field(default_factory=list)
    meeting_notes: list[MeetingNote] = field(default_factory=list)
    existing_reminders: list[dict[str, str]] = field(default_factory=list)
    collection_errors: list[str] = field(default_factory=list)

    def to_context_dict(self) -> dict[str, Any]:
        return {
            "emails": [e.__dict__ for e in self.emails],
            "calendar_events": [e.__dict__ for e in self.calendar_events],
            "meeting_notes": [m.__dict__ for m in self.meeting_notes],
            "existing_reminders": self.existing_reminders,
            "collection_errors": self.collection_errors,
        }
