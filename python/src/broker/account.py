from abc import ABC

from src.core.logger import create_logger

logger = create_logger(__name__)


class Account(ABC):
    """Account abstract class."""

    def __init__(self, initial_amount: float):
        """Initialize.

        Args:
            initial_amount: initial money amount.
        """
        self.amount = initial_amount
        logger.info(f"Account init. amount: {initial_amount}")
