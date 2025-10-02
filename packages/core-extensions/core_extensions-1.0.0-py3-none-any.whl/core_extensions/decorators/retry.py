# -*- coding: utf-8 -*-

"""
This module provides a flexible retry mechanism based on the tenacity library,
allowing for advanced retry strategies with exponential backoff, custom exception
handling, and detailed logging.

.. code-block:: python

    from core_extensions.decorators.retry import SimpleRetry

    # Basic usage with default settings
    retry_handler = SimpleRetry(max_attempts=3, base_delay=1.0)

    @retry_handler.create_decorator((ConnectionError, TimeoutError))
    def fetch_data():
        # Function that may fail transiently
        return api.get_data()

    # Advanced usage with custom logger and settings
    import logging

    custom_logger = logging.getLogger(__name__)
    retry_handler = SimpleRetry(
        max_attempts=5,
        base_delay=2.0,
        max_delay=30.0,
        reraise=False,
        logger=custom_logger
    )

    @retry_handler.create_decorator((ValueError, RuntimeError), reraise=True)
    def process_data():
        # Function with custom retry behavior
        pass
..
"""

from logging import Logger
from typing import Any
from typing import Callable
from typing import Optional
from typing import Tuple
from typing import Type

from core_mixins.logger import get_logger
from tenacity import RetryCallState
from tenacity import retry
from tenacity import retry_if_exception_type
from tenacity import stop_after_attempt
from tenacity import wait_exponential


class SimpleRetry:
    """
    Simple and generic retry mechanism based on `tenacity` library
    in case an advanced retry mechanism is required beyond simple capabilities
    offered by `core_mixins.decorators.retry`.
    """

    def __init__(
        self,
        max_attempts: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 10.0,
        reraise: bool = True,
        logger: Optional[Logger] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the SimpleRetry instance.

        :param max_attempts: Maximum number of retry attempts. Defaults to 3.
        :param base_delay: Base delay in seconds for exponential backoff. Defaults to 1.0.
        :param max_delay: Maximum delay in seconds between retries. Defaults to 10.0.

        :param reraise:
            Whether to reraise the exception after all retry attempts are exhausted.
            Defaults to True. If False, `tenacity.RetryError` is raised.

        :param logger: Optional custom logger instance. If None, a default logger will be created.
        :param kwargs: Additional keyword arguments to pass to tenacity.retry decorator.
        """

        if logger is None:
            logger = get_logger(
                logger_name=None,
                reset_handlers=True,
                propagate=False,
            )

        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.reraise = reraise
        self.logger = logger

        # Extra parameters to pass to `tenacity.retry`...
        self._kwargs = kwargs

    def after_error(self, ref: RetryCallState):
        """
        Callback executed after each failed attempt. It logs the exception
        type that caused the failure using info level to prevent
        error notifications while retrying.

        :param ref: RetryCallState containing information about the retry attempt.
        """

        if ref.outcome:
            exc = ref.outcome.exception()
            if exc:
                self.logger.info(
                    f"Error found: {exc.__class__.__name__}."
                )

    def before_sleep(self, ref: RetryCallState):
        """
        Callback executed before sleeping between retry attempts. It
        logs the retry attempt number, function name, and wait time.

        :param ref: RetryCallState containing information about the retry attempt.
        """

        fn_name = ref.fn.__name__ if ref.fn else "unknown"
        self.logger.info(
            f"Attempt # {ref.attempt_number} -> "
            f"Retrying function {fn_name} "
            f"after {ref.idle_for}."
        )

    def create_decorator(
        self,
        exception_types: Tuple[Type[Exception], ...],
        reraise: Optional[bool] = None,
    ) -> Callable:
        """
        Create a retry decorator for specified exception types.

        :param exception_types: Tuple of exception types to catch and retry on.
        :param reraise:
            Optional override for whether to reraise exceptions after all attempts.
            If None, uses the instance's reraise setting. If False, `tenacity.RetryError`
            is raised.

        :return: A tenacity retry decorator configured with the instance's settings.
        """

        return retry(
            stop=stop_after_attempt(self.max_attempts),
            wait=wait_exponential(multiplier=self.base_delay, max=self.max_delay),
            retry=retry_if_exception_type(exception_types),
            reraise=reraise if reraise is not None else self.reraise,
            before_sleep=self.before_sleep,
            after=self.after_error,
            **self._kwargs,
        )
