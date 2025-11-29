from dataclasses import dataclass


@dataclass
class LLMRequest:
    def __init__(self):
        self.prompt: str | None = None
        self.model: str | None = None
        self.temperature: float | None = None
        self.max_tokens: int | None = None
        self.system_prompt: str | None = None


class LLMRequestBuilder:
    def __init__(self):
        self.request = LLMRequest()

    def set_prompt(self, prompt: str):
        self.request.prompt = prompt
        return self

    def set_model(self, model: str):
        self.request.model = model
        return self

    def set_temperature(self, temperature: float):
        self.request.temperature = temperature
        return self

    def set_max_tokens(self, max_tokens: int):
        self.request.max_tokens = max_tokens
        return self

    def set_system_prompt(self, system_prompt: str):
        self.request.system_prompt = system_prompt
        return self

    def build(self) -> LLMRequest:
        return self.request


if __name__ == "__main__":
    builder = LLMRequestBuilder()
    request1 = (
        builder.set_prompt("Привет!")
        .set_model("gpt-5")
        .set_temperature(0.3)
        .set_max_tokens(512)
        .set_system_prompt("Ты помощник по программированию")
        .build()
    )

    print(request1.prompt)

    request2 = (
        LLMRequestBuilder()
        .set_prompt("Что такое жизнь?")
        .set_model("claude-4.5-sonnet")
        .set_temperature(0.6)
        .set_max_tokens(1024)
        .build()
    )

    print(request2.prompt)
