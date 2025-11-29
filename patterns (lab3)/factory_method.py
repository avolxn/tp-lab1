from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class OpenAIProvider(LLMProvider):
    def generate(self, prompt: str) -> str:
        return f"OpenAI GPT: {prompt}"


class AnthropicProvider(LLMProvider):
    def generate(self, prompt: str) -> str:
        return f"Anthropic Claude: {prompt}"


class LLMService(ABC):
    @abstractmethod
    def create_provider(self) -> LLMProvider:
        pass

    def process_request(self, prompt: str) -> str:
        return self.create_provider().generate(prompt)


class OpenAIService(LLMService):
    def create_provider(self) -> LLMProvider:
        return OpenAIProvider()


class AnthropicService(LLMService):
    def create_provider(self) -> LLMProvider:
        return AnthropicProvider()


if __name__ == "__main__":
    openai = OpenAIService()
    anthropic = AnthropicService()

    print(openai.process_request("Привет!"))
    print(anthropic.process_request("Как дела?"))
