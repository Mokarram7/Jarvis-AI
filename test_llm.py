from app.ai.llm import JarvisLLM

ai = JarvisLLM()

reply = ai.ask("Who are you?")

print(reply)