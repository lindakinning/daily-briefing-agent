#!/usr/bin/env python3
"""One-time Google OAuth setup for live data collection."""

from ea_workshop.collectors.google_live import SCOPES, _load_credentials
from ea_workshop.config import AppConfig


def main() -> None:
    config = AppConfig.load()
    creds_path = config.path(config.raw["google"]["credentials_path"])
    if not creds_path.exists():
        print(f"Missing {creds_path}")
        print("Download OAuth desktop credentials from Google Cloud Console.")
        print("See FINISH-ON-YOUR-OWN.md for step-by-step instructions.")
        raise SystemExit(1)

    print("Opening browser for Google sign-in...")
    _load_credentials(config)
    print("Success! Token saved. Run: ea-workshop")


if __name__ == "__main__":
    main()
