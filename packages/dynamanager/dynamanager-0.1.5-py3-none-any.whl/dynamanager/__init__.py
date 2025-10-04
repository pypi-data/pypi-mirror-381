"""Straightforward application config management powered by Dynaconf."""

from loguru import logger

from dynamanager.manager import ConfigContainer, Dynamanager

logger.disable("dynamanager")

# Placeholder for poetry-dynamic-versioning, do not change:
# https://github.com/mtkennerly/poetry-dynamic-versioning#installation
__version__ = "0.1.5"

__all__ = ["ConfigContainer", "Dynamanager"]
