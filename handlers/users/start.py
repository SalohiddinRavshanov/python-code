from aiogram import types
import asyncpg
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from keyboards.inline.checksub import inline
from data.config import ADMINS
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.misc.subscribtion import check
from aiogram.types import CallbackQuery
from loader import dp , bot
from utils.misc.subscribtion import check
from keyboards.default.keyboard import bosh_sahifa


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def video_file(message:types.video):
    file_id = message.video.file_id
    await message.answer(file_id)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    # try:
    #     user = await db.add_user(telegram_id=message.from_user.id,
    #                              full_name=message.from_user.full_name,
    #                              username=message.from_user.username,
    #                              )
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await db.select_user(telegram_id = message.from_user.id)


    # users = await db.count_users()
    # msg = f"Bazaga {user[1]} qoshildi , bazada {users} ta odam bor!"

    # await bot.send_message(chat_id=ADMINS[0],text=msg)
    await message.answer(f'salom botga xush kelibsiz!\n'
                                  f'✅ Botdan to\'liq foydalanishingiz mumkin!', reply_markup=bosh_sahifa)
