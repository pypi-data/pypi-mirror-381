import logging
import os

try:
    from coloredlogs import ColoredFormatter as Formatter
except ModuleNotFoundError:
    from logging import Formatter

LOGGER_DATEFMT = "%Y-%m-%d %H:%M:%S"


def configure_logger(name, logger=None, log_level=logging.INFO):
    """Set up common logging settings for the `logging.Logger`.

    If a logger is not provided, configure the root logger instead.

    """
    log_format = f"[%(asctime)-15s] {name} | %(name)s | %(levelname)+8s | %(message)s"
    if "LOG_LEVEL" in os.environ:
        log_level = os.environ["LOG_LEVEL"]

    if not logger:
        logger = logging.getLogger()
    logger.setLevel(log_level)
    handler = logging.StreamHandler()
    handler.setFormatter(Formatter(
        fmt=log_format,
        datefmt=LOGGER_DATEFMT,
    ))
    logger.addHandler(handler)

    # configure non-root loggers not managed by this package
    other_log_level = max(log_level, logging.WARNING)
    logging.getLogger("kafka").setLevel(other_log_level)
    logging.getLogger("watchdog").setLevel(other_log_level)
