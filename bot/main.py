from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
import database
import handlers.Start
import handlers.Category
import handlers.User

api = config.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.message_handler(commands=['start'])(handlers.Start.start)
dp.callback_query_handler(text='formulas')(handlers.Start.get_formulas)
dp.message_handler(text="Информация")(handlers.Start.start_message)

dp.message_handler(text='Купить')(handlers.Category.get_buying_list)
dp.callback_query_handler(text='product_buying')(handlers.Category.send_confirm_message)
dp.message_handler(text='Рассчитать')(handlers.Category.main_menu)
dp.callback_query_handler(text='calories')(handlers.Category.set_age)
dp.message_handler(state=handlers.Category.UserState.age)(handlers.Category.set_growth)
dp.message_handler(state=handlers.Category.UserState.growth)(handlers.Category.set_weight)
dp.message_handler(state=handlers.Category.UserState.weight)(handlers.Category.send_calories)

dp.message_handler(text="Регистрация")(handlers.User.sing_up)
dp.message_handler(state=handlers.User.RegistrationState.username)(handlers.User.set_username)
dp.message_handler(state=handlers.User.RegistrationState.email)(handlers.User.set_email)
dp.message_handler(state=handlers.User.RegistrationState.age)(handlers.User.set_age)

dp.message_handler()(handlers.Start.all_message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

