import logging
import os

def setup_logger():
    logger = logging.getLogger("UDS_Framework")

    if logger.hasHandlers():
        return logger  # Prevent duplicate handlers

    logger.setLevel(logging.DEBUG)

    # Create logs directory if not exists
    os.makedirs("logs", exist_ok=True)

    file_handler = logging.FileHandler("logs/uds_log.log", mode = "w")
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger