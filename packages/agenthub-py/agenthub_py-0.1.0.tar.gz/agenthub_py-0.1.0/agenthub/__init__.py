"""
AgentHub SDK - Lighweight interface to make agents runnable in simulation environment.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List

__version__ = "0.1.0"
__all__ = ["AgentRunner"]


class AgentRunner(ABC):
    """
    Abstract base class for AI agent runners.

    This class defines the interface that all AI agents must implement to be used
    within the agent runtime environment. Subclasses must implement the `run` method
    to process input and return a JSON-serializable result.
    """

    @abstractmethod
    def run(self, input_data: Dict[str, Any] | List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Process the input data and return a result.

        Args:
            input_data: A dictionary containing the input data for the agent.

        Returns:
            A dictionary containing the result of the agent's processing.
            The dictionary must be JSON-serializable.

        Raises:
            Exception: If there is an error during processing.
        """
        pass