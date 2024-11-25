from bot.keyboards import *
from bot.database import *
from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

async def set_username(message, state):
    await state.update_data(username=message.text)
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data["username"], data["email"], data["age"])
    await state.finish()