import os
from ._http import HTTPClient
from .embeddings import Embeddings
from .evaluator import Evaluator

class ProtonX:
    """
    ProtonX SDK entrypoint (similar to openai.OpenAI)
    """

    def __init__(self, base_url: str = None, api_key: str = None):
        base_url = base_url or os.getenv("PROTONX_API_URL", "https://embeddings.protonx.io")
        api_key = api_key or os.getenv("PROTONX_API_KEY")

        self.http = HTTPClient(base_url=base_url, api_key=api_key)
        self.embeddings = Embeddings(self.http)

    def evals(self):
        """Return an Evaluator instance for LLM response evaluation"""
        return Evaluator(self.http)
    
    
