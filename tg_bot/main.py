import os
import aiohttp
import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '7159959429:AAH2CNlJ0R-S3V1Dm8ltrc8JCC2TXN2agLY')
SERVER_URI = os.getenv('SERVER_URI', 'http://127.0.0.1/telegram-auth/')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart)
async def start_command(message: Message):
    payload = {
        'id': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(SERVER_URI, data=payload) as response:
            if response.status == 200:
                response_json = await response.json()
                token = response_json.get('token')
                await message.reply(f'Для завершения авторизации перейдите на страницу{SERVER_URI}?token={token}')
            else:
                await message.reply(f'Ошибка авторизации {response.text}')


async def start_polling():
    while True:
        try:
            await dp.start_polling(bot)
        except Exception:
            pass

if __name__ == '__main__':
    while True:
        try:
            asyncio.run(start_polling())
        except Exception:
            pass
