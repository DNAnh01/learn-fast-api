import logging

import colorlog


def setup_logger() -> logging.Logger:
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)s:%(name)s:%(pathname)s:%(funcName)s:%(message)s",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green, bg_white",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
                "EXCEPTION": "purple",
            },
        )
    )

    logger = colorlog.getLogger(__name__)
    logger.addHandler(handler)

    logger.setLevel(logging.DEBUG)

    return logger
