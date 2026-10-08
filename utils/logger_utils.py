import logging
from datetime import datetime
from pathlib import Path


class LoggerUtils:
    LOG_DIR = Path("logs")
    LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def configure_logging():
        LoggerUtils.LOG_DIR.mkdir(exist_ok=True)
        log_file = LoggerUtils.LOG_DIR / f"pytest_{datetime.now():%Y%m%d_%H%M%S}.log"

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        formatter = logging.Formatter(LoggerUtils.LOG_FORMAT, LoggerUtils.DATE_FORMAT)

        file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        root_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        root_logger.addHandler(console_handler)

        return log_file
