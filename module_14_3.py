from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = '7312413520:AAFQQj0X0WQIU0IKaeH6O7qprE_aFq1BuEc'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text = "Рассчитать")
button2 = KeyboardButton(text = "Информация")
button3 = KeyboardButton(text = "Купить")
kb.row(button1, button2)
kb.add(button3)

kb2 = InlineKeyboardMarkup()
button4 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button5 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
kb2.add(button4)
kb2.add(button5)

pr_kb=InlineKeyboardMarkup(resize_keyboard=True)
pr_button1=InlineKeyboardButton(text='Product1', callback_data='product_buying')
pr_button2=InlineKeyboardButton(text='Product2', callback_data='product_buying')
pr_button3=InlineKeyboardButton(text='Product3', callback_data='product_buying')
pr_button4=InlineKeyboardButton(text='Product4', callback_data='product_buying')
pr_kb.row(pr_button1, pr_button2, pr_button3, pr_button4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f'Название: Product{i}| Описание: описание{i}| Цена: {i*100}')
        with open(f'product_photo/{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=pr_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = kb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Упрощенный вариант формулы Миффлина-Сан Жеора для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler(text="Информация")
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Подберу норму калорий для тебя!')

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма калорий {result} в день' )
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)