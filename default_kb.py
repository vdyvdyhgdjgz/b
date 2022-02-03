from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#ReplyKeyboardRemowe

b1 = KeyboardButton('/Msk')
#b2 = KeyboardButton('/Другой_город')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1)
#add(b2)
