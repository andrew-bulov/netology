import logging as log
import sys

from fastapi import FastAPI

from app.api.users import router as users_router
from app.core.config import ENV_NAME, LOG_LEVEL
from app.core.logging import setup_logging

setup_logging()
app = FastAPI()
app.include_router(users_router)
print("PYTHON:", sys.executable)
print("ENV:", ENV_NAME)
print("LOG_LEVEL:", LOG_LEVEL)


@app.get("/health")
def health():
    log.debug("Requested health status")
    return {"status": "ok"}
