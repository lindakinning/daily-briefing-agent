from __future__ import annotations

import argparse
import logging
import sys

from ea_workshop.collectors import collect_live, load_sample_data
from ea_workshop.config import AppConfig
from ea_workshop.synthesizer import synthesize
from ea_workshop.writers.markdown import write_markdown_brief


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def run(*, sample: bool = False, dry_run: bool = False) -> int:
    config = AppConfig.load()
    setup_logging()
    logger = logging.getLogger(__name__)

    if sample:
        logger.info("Using sample data (no Google OAuth required)")
        data = load_sample_data(config)
    else:
        logger.info("Collecting live data from Google")
        data = collect_live(config)

    result = synthesize(config, data)
    path = write_markdown_brief(config, result, dry_run=dry_run)

    if dry_run:
        logger.info("Dry run complete (printed above)")
    else:
        logger.info("Wrote brief to %s", path)
        logger.info("Tasks suggested: %d", len(result.tasks))
        logger.info("Next: add a task writer — see FINISH-ON-YOUR-OWN.md")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="EA Workshop — morning brief agent")
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Use bundled sample data (no Google setup)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print brief to terminal; don't write file",
    )
    args = parser.parse_args()
    return run(sample=args.sample, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
