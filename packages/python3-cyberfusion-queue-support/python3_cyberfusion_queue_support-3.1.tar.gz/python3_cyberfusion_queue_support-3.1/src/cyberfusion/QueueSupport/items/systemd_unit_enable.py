"""Item."""

import logging
from typing import List, Optional

from cyberfusion.QueueSupport.items import _Item
from cyberfusion.QueueSupport.outcomes import (
    SystemdUnitEnableItemEnableOutcome,
)
from cyberfusion.SystemdSupport.units import Unit

logger = logging.getLogger(__name__)


class SystemdUnitEnableItem(_Item):
    """Represents item."""

    def __init__(
        self,
        *,
        name: str,
        reference: Optional[str] = None,
        hide_outcomes: bool = False,
        fail_silently: bool = False,
    ) -> None:
        """Set attributes."""
        self.name = name
        self._reference = reference
        self._hide_outcomes = hide_outcomes
        self._fail_silently = fail_silently

        self.unit = Unit(self.name)

    @property
    def outcomes(self) -> List[SystemdUnitEnableItemEnableOutcome]:
        """Get outcomes of item."""
        outcomes = []

        if not self.unit.is_enabled:
            outcomes.append(SystemdUnitEnableItemEnableOutcome(unit=self.unit))

        return outcomes

    def fulfill(self) -> List[SystemdUnitEnableItemEnableOutcome]:
        """Fulfill outcomes."""
        outcomes = self.outcomes

        for outcome in outcomes:
            outcome.unit.enable()

        return outcomes

    def __eq__(self, other: object) -> bool:
        """Get equality based on attributes."""
        if not isinstance(other, SystemdUnitEnableItem):
            return False

        return other.name == self.name
