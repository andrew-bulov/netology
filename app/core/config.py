import os
from pathlib import Path

from dotenv import load_dotenv

ENV_NAME = os.getenv("ENV", "local")

env_file = Path(f".env.{ENV_NAME}")
if env_file.exists():
    load_dotenv(env_file)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_SQL = os.getenv("LOG_SQL", "false").lower() == "true"
