"""
PublicationError module.
"""

from .domain_event_pattern_base_error import DomainEventPatternBaseError
from .handler_error import HandlerError


class PublicationError(DomainEventPatternBaseError):
    """
    Exception raised when there is an error during the publication of domain events.
    """

    _errors: list[HandlerError]

    def __init__(self, *, errors: list[HandlerError]) -> None:
        """
        Initialize the PublicationError.

        Args:
            errors (list[HandlerError]): The list of handler errors that occurred.

        Example:
        ```python
        # TODO:
        ```
        """
        self._errors = errors

        message = f'There were {len(errors)} errors during the events publication.'
        super().__init__(message=message)

    @property
    def errors(self) -> list[HandlerError]:
        """
        Get the errors that occurred during publication.

        Returns:
            list[HandlerError]: The list of handler errors that occurred.

        Example:
        ```python
        # TODO:
        ```
        """
        return self._errors
