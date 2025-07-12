import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from handlers import get_gpt_reply
from tts import synthesize_text
from stt import transcribe_audio

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Welcome to English Park! Send a message or voice note to begin learning.")

@dp.message_handler(content_types=types.ContentType.VOICE)
async def handle_voice(message: types.Message):
    file_info = await bot.get_file(message.voice.file_id)
    file = await bot.download_file(file_info.file_path)
    with open("voice.ogg", "wb") as f:
        f.write(file.read())
    text = transcribe_audio("voice.ogg")
    reply = get_gpt_reply(text)
    audio_file = synthesize_text(reply)
    await message.answer(reply)
    await bot.send_voice(message.chat.id, voice=open(audio_file, "rb"))

@dp.message_handler()
async def handle_text(message: types.Message):
    reply = get_gpt_reply(message.text)
    audio_file = synthesize_text(reply)
    await message.answer(reply)
    await bot.send_voice(message.chat.id, voice=open(audio_file, "rb"))

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
