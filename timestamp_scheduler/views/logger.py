"""
View module for logging events.
"""

import logging
from config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_message(message):
    print(message)
    logging.info(message)
