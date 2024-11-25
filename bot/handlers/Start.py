from bot.keyboards import *

async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Подберу норму калорий для тебя!')

async def get_formulas(call):
    await call.message.answer('Упрощенный вариант формулы Миффлина-Сан Жеора для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')