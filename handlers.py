from config import *
import openai

openai.api_key = OPENAI_API_KEY

def get_gpt_reply(message):
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": "You are an English tutor."},
            {"role": "user", "content": message},
        ],
        max_tokens=MAX_GPT_TOKENS
    )
    return response['choices'][0]['message']['content']
