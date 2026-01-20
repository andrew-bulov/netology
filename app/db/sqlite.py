import sqlite3
import logging

from app.core.config import LOG_SQL

sql_logger = logging.getLogger("sql")


def get_connection(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)

    if LOG_SQL:
        conn.set_trace_callback(sql_logger.debug)

    return conn
