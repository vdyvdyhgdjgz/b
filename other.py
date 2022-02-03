import requests
import datetime
from aiogram.utils import executor
from aiogram import types, Dispatcher
from create_bot import dp



#@dp.message_handler()
async def get_weather(message: types.Message):
	code_to_smile = {
		"Clear": "Ясно \U00002600",
		"Clouds": "Облачно \U00002601",
		"Rain": "Дождь \U00002614",
		"Drizzle": "Дождь \U00002614",
		"Thunderstorm": "Гроза \U000026A1",
		"Snow": "Снег \U0001F328",
		"Mist": "Туман \U0001F32B"
	}
	try:
		r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
		data = r.json()

		city = data["name"]
		cur_weather = data["main"]["temp"]
		like = data["main"]["feels_like"]
		t_max = data["main"]["temp_max"]
		t_min = data["main"]["temp_min"]
		weather_description = data["weather"][0]["main"]
		if weather_description in code_to_smile:
			wd = code_to_smile[weather_description]
		else:
			wd = "Посмотри в окно, не пойму что там за погода!"
		humidity = data["main"]["humidity"]
		pressure = data["main"]["pressure"]
		wind = data["wind"]["speed"]
		wind_gust = data["wind"]["gust"]
		wind_deg = data["wind"]["deg"]
		sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
		sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
		length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
			data["sys"]["sunrise"])

		await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
			f"Погода в городе: {city} {wd}\n"
			f"Ощущаемая температура {like}C°\n"
			f"Температура: {cur_weather}C°\n"
			f"t_max: {t_max}C° t_min {t_min}C°\n"
			f"Влажность: {humidity}%  Давление: {pressure}Па\n"
			f"Ветер: {wind}м/с Порывы до: {wind_gust}м/с\n"
			f"Направление ветра: {wind_deg}°\n"
			f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
			f"***Хорошей погоды!***"
	except:
		await message.reply("\U00002620 Кривое название города \U00002620")
