import asyncio
import edge_tts

async def text_to_speech(text, output_path="narration.mp3", voice="en-US-GuyNeural"):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)
    return output_path

def create_audio(text, output_path="narration.mp3"):
    asyncio.run(text_to_speech(text, output_path))
    return output_path
