"""Autumn SDK - A simple Python SDK for Autumn."""

__version__ = "0.1.0"


class AutumnClient:
    """Simple Autumn client."""

    def __init__(self, api_key: str):
        """Initialize the Autumn client.
        
        Args:
            api_key: Your Autumn API key
        """
        self.api_key = api_key

    def hello(self) -> str:
        """Return a simple greeting.
        
        Returns:
            A greeting string
        """
        return "Hello from Autumn SDK!"


__all__ = ["AutumnClient", "__version__"]
