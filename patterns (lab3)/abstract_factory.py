from abc import ABC, abstractmethod


class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class OpenAIClient(LLMClient):
    def generate(self, prompt: str) -> str:
        return f"[OpenAI] {prompt} → generated response"


class YandexGPTClient(LLMClient):
    def generate(self, prompt: str) -> str:
        return f"[YandexGPT] {prompt} → generated response"


class LLMFactory(ABC):
    @abstractmethod
    def create_client(self) -> LLMClient:
        pass


class OpenAIFactory(LLMFactory):
    def create_client(self) -> LLMClient:
        return OpenAIClient()


class YandexGPTFactory(LLMFactory):
    def create_client(self) -> LLMClient:
        return YandexGPTClient()


def run_inference(factory: LLMFactory, prompt: str):
    client = factory.create_client()
    return client.generate(prompt)


if __name__ == "__main__":
    openai_factory = OpenAIFactory()
    yandexgpt_factory = YandexGPTFactory()

    openai_result = run_inference(openai_factory, "Explain quantum computing.")
    yandexgpt_result = run_inference(yandexgpt_factory, "Explain quantum computing.")

    print(openai_result)
    print(yandexgpt_result)
