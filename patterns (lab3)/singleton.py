class LLM:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not LLM._initialized:
            self.model_name = "gpt-oss-20b"
            self.base_url = "https://openrouter.ai/api/v1"
            LLM._initialized = True

    def invoke(self, prompt: str) -> str:
        return f"LLM {self.model_name} ({self.base_url}) отвечает на '{prompt}'..."


if __name__ == "__main__":
    llm1 = LLM()
    llm2 = LLM()

    print(f"llm1 is llm2: {llm1 is llm2}")
    print(llm1.invoke("Привет, LLM!"))
    print(llm2.invoke("Расскажи шутку!"))
