"""
DomainEventPatternBaseError module.
"""

from abc import ABC
from typing import Any, Self


class DomainEventPatternBaseError(Exception, ABC):
    """
    DomainEventPatternBaseError class is the base for all custom errors.
    """

    _message: str

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        """
        Creates a new instance of the DomainEventPatternBaseError.

        Args:
            *args (Any): Positional arguments for the error.
            **kwargs (Any): Keyword arguments for the error.

        Raises:
            TypeError: If the class is DomainEventPatternBaseError.

        Returns:
            Self: A new instance of the DomainEventPatternBaseError.
        """
        if cls is DomainEventPatternBaseError:
            raise TypeError(f'Cannot instantiate abstract class <<<{cls.__name__}>>>.')

        return super().__new__(cls)

    def __init__(self, *, message: str) -> None:
        """
        Initializes the DomainEventPatternBaseError with a message.

        Args:
            message (str): The error message.
        """
        self._message = message

        super().__init__(self._message)

    @property
    def message(self) -> str:
        """
        Returns the error message.

        Returns:
            str: The error message.
        """
        return self._message
