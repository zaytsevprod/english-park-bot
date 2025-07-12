from aiogram import Dispatcher, types
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def start_handler(message: types.Message):
    await message.reply("Привет! Я помогу тебе улучшить твой английский язык. Напиши мне что-нибудь!")

async def practice_handler(message: types.Message):
    prompt = f"Correct this English and give a brief explanation:\n\n{message.text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
    )
    corrected = response["choices"][0]["message"]["content"]
    await message.reply(corrected)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(practice_handler)
