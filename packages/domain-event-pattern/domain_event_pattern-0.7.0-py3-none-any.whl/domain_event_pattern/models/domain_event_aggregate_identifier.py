"""
DomainEventAggregateIdentifier module.
"""

from value_object_pattern.usables.identifiers import StringUuidV4ValueObject


class DomainEventAggregateIdentifier(StringUuidV4ValueObject):
    """
    Value object for domain event aggregate identifier.
    """
