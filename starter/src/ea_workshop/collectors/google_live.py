from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from ea_workshop.config import AppConfig
from ea_workshop.models import CalendarEvent, CollectedData, EmailSummary

logger = logging.getLogger(__name__)

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar.readonly",
]


def _load_credentials(config: AppConfig) -> Credentials:
    token_path = config.path(config.raw["google"]["token_path"])
    creds_path = config.path(config.raw["google"]["credentials_path"])

    if token_path.exists():
        return Credentials.from_authorized_user_file(str(token_path), SCOPES)

    flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
    creds = flow.run_local_server(port=0)
    token_path.parent.mkdir(parents=True, exist_ok=True)
    token_path.write_text(creds.to_json(), encoding="utf-8")
    return creds


def collect_google_data(config: AppConfig) -> CollectedData:
    creds = _load_credentials(config)
    data = CollectedData()

    gmail = build("gmail", "v1", credentials=creds)
    query = config.raw["google"]["gmail_query"]
    results = gmail.users().messages().list(userId="me", q=query, maxResults=25).execute()

    for item in results.get("messages", []):
        msg = gmail.users().messages().get(userId="me", id=item["id"], format="metadata").execute()
        headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
        data.emails.append(
            EmailSummary(
                id=msg["id"],
                subject=headers.get("Subject", "(no subject)"),
                sender=headers.get("From", ""),
                snippet=msg.get("snippet", ""),
                date=headers.get("Date", ""),
                is_unread="UNREAD" in msg.get("labelIds", []),
                is_starred="STARRED" in msg.get("labelIds", []),
                account="Work",
            )
        )

    calendar = build("calendar", "v3", credentials=creds)
    now = datetime.now(timezone.utc)
    hours = int(config.raw["google"].get("calendar_hours_ahead", 36))
    end = now + timedelta(hours=hours)
    events = (
        calendar.events()
        .list(
            calendarId="primary",
            timeMin=now.isoformat(),
            timeMax=end.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    for event in events.get("items", []):
        start = event.get("start", {}).get("dateTime", event.get("start", {}).get("date", ""))
        end_time = event.get("end", {}).get("dateTime", event.get("end", {}).get("date", ""))
        data.calendar_events.append(
            CalendarEvent(
                id=event["id"],
                title=event.get("summary", "(no title)"),
                start=start,
                end=end_time,
                location=event.get("location", ""),
                account="Work",
            )
        )

    logger.info(
        "Collected %d emails and %d calendar events",
        len(data.emails),
        len(data.calendar_events),
    )
    return data
