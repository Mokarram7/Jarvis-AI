from app.ai.memory import Memory

memory = Memory()

memory.save("name", "Mokarram")

print(memory.recall("name"))