import requests
from django.conf import settings


class LLM:
    def __init__(self):
        self.api_base = getattr(settings, "SEMANTIC_SEARCH_EMBEDDING_API_BASE_URL")
        self.api_key = getattr(settings, "SEMANTIC_SEARCH_EMBEDDING_API_KEY")
        self.model_name = getattr(settings, "SEMANTIC_SEARCH_EMBEDDING_MODEL")
        self.dimensions = getattr(settings, "SEMANTIC_SEARCH_NUM_DIMENSIONS", 768)
        self.session = requests.Session()

    def get_embeddings(self, texts, *, prompt_name=None) -> list[list[float]]:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"input": texts, "model": self.model_name, "dimensions": self.dimensions}
        if prompt_name:
            data["type"] = prompt_name

        num_retries = 0
        while num_retries < 5:
            response = self.session.post(
                f"{self.api_base}/embeddings", json=data, headers=headers
            )
            if response.status_code == 200:
                break
            num_retries = num_retries + 1

        if num_retries == 5:
            raise Exception("get_embeddings call failed too many times")

        payload = response.json()
        results = payload.get("data", [])
        embeddings = [result.get("embedding") for result in results]

        return embeddings


llm = LLM()
