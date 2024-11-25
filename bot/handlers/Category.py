from bot.keyboards import *
from bot.database import *
from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(get_all_products(i))
        with open(f'C:/Users/egorp/PycharmProjects/pythonProject1/bot/files/{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=pr_kb)


async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = kb2)


async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()


async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма калорий {result} в день' )
    await state.finish()
