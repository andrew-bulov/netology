# app/core/logging.py
import logging
from app.core.config import LOG_LEVEL, ENV_NAME


def setup_logging() -> None:
    logging.basicConfig(
        level=LOG_LEVEL,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s | env=%(env)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.getLogger("sql").setLevel(logging.DEBUG)
    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.env = ENV_NAME
        return record

    logging.setLogRecordFactory(record_factory)
