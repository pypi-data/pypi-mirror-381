"""Public package interface and logging helpers for the Oireachtas API wrapper."""

import logging
from typing import Optional

from .api import API as API
from .wrapper import Wrapper as Wrapper


DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def configure_logging(
    *,
    level: int = logging.DEBUG,
    filename: Optional[str] = 'OireachtasWrapper_API.log',
    fmt: str = DEFAULT_LOG_FORMAT,
) -> None:
    """Opt-in helper to configure logging for users of the wrapper.

    Parameters mirror :func:`logging.basicConfig` while providing sensible
    defaults for consumers that want file-based logging for API interactions.
    """

    logging.basicConfig(filename=filename, level=level, format=fmt)
