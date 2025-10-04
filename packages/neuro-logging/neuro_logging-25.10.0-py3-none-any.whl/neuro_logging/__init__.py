import logging
import logging.config
import os
import typing as t
from importlib.metadata import version

from pythonjsonlogger.orjson import OrjsonFormatter

from .config import EnvironConfigFactory
from .trace import (
    new_sampled_trace,
    new_trace,
    new_trace_cm,
    notrace,
    setup_sentry,
    trace,
    trace_cm,
)

__version__ = version(__package__)

__all__ = [
    "init_logging",
    "AllowLessThanFilter",
    "notrace",
    "setup_sentry",
    "trace",
    "trace_cm",
    "new_sampled_trace",
    "new_trace",
    "new_trace_cm",
]


class AllowLessThanFilter(logging.Filter):
    def __init__(self, level: t.Union[int, str] = logging.ERROR, name: str = ""):
        super().__init__(name)
        if not isinstance(level, int):
            try:
                level = logging._nameToLevel[level]
            except KeyError:
                raise ValueError(f"Unknown level name: {level}")
        self.level = level

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno < self.level


class _HealthCheckFilter(logging.Filter):
    def __init__(self, url_path: str = "/api/v1/ping", name: str = "") -> None:
        super().__init__(name)
        self.url_path = url_path

    def filter(self, record: logging.LogRecord) -> bool:
        if record.levelno > logging.INFO:
            return True
        return record.getMessage().find(self.url_path) == -1


BASE_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
        "json": {
            "()": OrjsonFormatter,
            "reserved_attrs": [
                "created",
                "exc_text",
                "levelno",
                "msecs",
                "msg",
                "relativeCreated",
            ],
            "rename_fields": {
                "name": "logName",
                "levelname": "severity",
                "extra": "jsonPayload",
            },
            "timestamp": True,
        },
    },
    "filters": {
        "hide_errors": {"()": AllowLessThanFilter, "level": "ERROR"},
        "hide_health_checks": {"()": _HealthCheckFilter},
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
            "filters": ["hide_errors"],
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "standard",
            "stream": "ext://sys.stderr",
        },
        "json": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "json",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "aiohttp.access": {
            "level": logging.NOTSET,
            "propagate": True,
            "filters": ["hide_health_checks"],
        },
        "uvicorn.access": {
            "level": logging.NOTSET,
            "propagate": True,
            "filters": ["hide_health_checks"],
        },
    },
}


TEXT_CONFIG = BASE_CONFIG | {
    "root": {
        "level": logging.DEBUG,
        "handlers": ["stderr", "stdout"],
    },
}

JSON_CONFIG = BASE_CONFIG | {
    "root": {
        "level": logging.DEBUG,
        "handlers": ["json"],
    },
}


def init_logging(
    *,
    health_check_url_path: str = "/api/v1/ping",
) -> None:
    config = EnvironConfigFactory().create_logging()
    if "PYTEST_VERSION" in os.environ:
        config_template = TEXT_CONFIG
    else:
        config_template = JSON_CONFIG
    dict_config: dict[str, t.Any] = config_template.copy()
    dict_config["root"]["level"] = config.log_level
    if config.log_health_check:
        dict_config["loggers"].pop("aiohttp.access", None)
        dict_config["loggers"].pop("uvicorn.access", None)
    dict_config["filters"]["hide_health_checks"]["url_path"] = health_check_url_path
    logging.config.dictConfig(dict_config)
