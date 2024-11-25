from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text = "Рассчитать")
button2 = KeyboardButton(text = "Информация")
button3 = KeyboardButton(text = "Купить")
button4 = KeyboardButton(text = "Регистрация")
kb.row(button1, button2)
kb.row(button3, button4)

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
