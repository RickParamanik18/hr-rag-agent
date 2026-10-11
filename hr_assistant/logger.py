import logging 
import os
from datetime import datetime

LOGS_DIR="logs"
os.makedirs(LOGS_DIR, exist_ok=True)

_run_started_at = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
RUN_LOG_FILE = os.path.join(LOGS_DIR, f"run_{_run_started_at}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(RUN_LOG_FILE),
        logging.StreamHandler()
    ]
)

def get_logger(name):
    logger = logging.getLogger(name)
    return logger