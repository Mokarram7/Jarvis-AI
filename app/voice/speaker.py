import asyncio
import edge_tts
import pygame
import os
import uuid


VOICE = "en-US-GuyNeural"


def speak(text):

    text = str(text)

    print(f"Jarvis: {text}")

    filename = f"{uuid.uuid4()}.mp3"

    async def generate():
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(filename)

    asyncio.run(generate())

    pygame.mixer.init()

    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()

    os.remove(filename)