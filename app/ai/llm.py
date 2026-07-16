import ollama


class JarvisLLM:

    def __init__(self):
        self.model = "qwen2.5:3b"

    def ask(self, prompt: str):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, an AI assistant. "
                        "Always reply in 2-3 short sentences. "
                        "Be concise and conversational."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]