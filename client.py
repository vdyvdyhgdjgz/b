from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

#@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Доброго дня, можно запросить текущую погоду в любом городе, просто указав название города боту.\n !Чистого неба всем!', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('С ботом бухтеть только в ЛС:\nhttps://t.me/Trener_good_bot')

async def command_help(message : types.Message):
	await bot.send_message(message.from_user.id, 'Можно получить погоду в любом городе просто написав название города боту')
#@dp.message_handler(commands=['Msk'])
async def pogoda_mur_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Тут будет погода')
	await message.delete()

#Хотел сделать, но передумал, можно просто название города боту написать
#@dp.message_handler(commands=['Luboi'])
#async def pogoda_alen_command(message : types.Message):
#	await bot.send_message(message.from_user.id, 'Погода в указанном городе')
#	await message.delete()

def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start'])
	dp.register_message_handler(command_help, commands=['help'])
	dp.register_message_handler(pogoda_mur_command, commands=['Msk'])
	dp.register_message_handler(pogoda_alen_command, commands=['Другой_город'])

