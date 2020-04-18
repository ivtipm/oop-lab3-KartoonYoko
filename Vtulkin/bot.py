import datetime
import re
import json
import requests
from basingBot import AbstractBot


class Bot(AbstractBot):
	""" Класс чат-бот.
		Умеет овечать на
			реплики-шаблолны:
				- Привет, бот!
				- В чем смысл жизни?
			простые команды:
				- Который час?
				- Сколько времени?
				- Какой год?
				- Погода
			команды с параметрами:
				- Умножь 12 на 157
				- Сложи 14 и 13
				- Раздели 67 на 4
				- Прибавь 78 к 87
		Умеет хранить историю сообщений, записывая историю в файл по завершению программы.
		И загружать из файла при запуске.

		Получение актуальной информации из интернета.
	"""

	@staticmethod
	def find_out_condition(condition: str):
		""" Перевести описание погоды для метода find_out_weather"""
		d = {"clear": "ясно", "partly-cloudy": "малооблачно", "cloudy": "облачно с прояснениями",
			"overcast": "пасмурно", "partly-cloudy-and-light-rain": "небольшой дождь", "partly-cloudy-and-rain": "дождь",
			"overcast-and-rain": "сильный дождь",  "overcast-thunderstorms-with-rain":
			"сильный дождь, гроза", "cloudy-and-light-rain":
			"небольшой дождь", "overcast-and-light-rain":
			"небольшой дождь","cloudy-and-rain":
			"дождь", "overcast-and-wet-snow":
			"дождь со снегом","partly-cloudy-and-light-snow":
			"небольшой снег","partly-cloudy-and-snow":
			"снег","overcast-and-snow":
			"снегопад","cloudy-and-light-snow":"небольшой снег",
			"overcast-and-light-snow": "небольшой снег","cloudy-and-snow": "снег"
			}
		if condition in d.keys():
			return d[condition]
		return "Непонятные условия погоды."

	def find_out_weather(self) -> str:
		""" Запрос погоды через Yandex API"""
		api_key = "ae76725b-fa0a-4b4e-a41b-38e5e8d03037"
		# широта и долгота нужного города (для Читы "52.033973" и "113.499432")
		lat = "52.033973"
		lon = "113.499432"
		try:
			headers = {'X-Yandex-API-Key': api_key}
			res = requests.get("https://api.weather.yandex.ru/v1/informers?lat={}&lon={}".format(lat, lon), headers=headers)
			# print(res.status_code)
			data = res.json()
			stroka = self.find_out_condition(str(data["fact"]['condition']))
			answer = "Температура (°C): " + str(data["fact"]["temp"]) + \
					 "\nОщущается как: " + str(data["fact"]['feels_like']) + \
					 "\n" + stroka + \
					 "\nВетер: " + str(data["fact"]['wind_speed']) + " м/c"
			return answer
		except Exception as e:
			return "Что-то пошло не так." + e

	def get_history_of_chatting(self) -> dict:
		return self._rec

	def write_to_json(self):
		""" Запись в файл"""
		with open("users/"+self._userName+".json", "w") as file:
			json.dump(self._rec, file, indent="")

	def read_from_json(self):
		""" Чтение из файла с именем пользователя"""
		try:
			with open("users/"+self._userName+".json", "r") as file:
				self._rec = json.load(file)
		except FileNotFoundError:
			self._rec = {}

	def fill_dict(self, key: str, data: list):
		""" ЗАполнить запись"""
		self._rec[key] = data

	def set_name_of_user(self, name: str):
		""" задает имя пользователя и ищет подходящий файл с историей сообщений"""
		if isinstance(name, str):
			self._userName = name
			self.read_from_json()

	def __init__(self, user_name: str = "user"):
		""" Конструктор для инициализации имени пользователя и истории сообщений"""
		self._userName = user_name  # Имя пользователя
		self._rec = {}
		self.read_from_json()  # инициализируется свойство _rec для хранения истории переписки в виде словаря

	def reply(self, s: str) -> str:
		""" Метод "ответа бота". Вернет строку с ответом. """
		if isinstance(s, str):
			answer = 0  # для ответа на арифметические вопросы
			now = datetime.datetime.now()  # текущее время
			s = s.lower()
			message = "Я Вас не понял, не могли бы Вы повторить?"

			# Приветствие в ответ на "Привет бот"
			match = re.search(r'(?:пр\w{,1}в\w{,1}т\w{,1}\s{,10}б\w{,2}т)', s)
			if match:
				message = "Привет, " + self._userName + "!"

			# шаблонное выражение для вывода времени
			match = re.search(r'(?:ск\w{,1}л\w{,1}к\w{,1}\s{,10}вр\w{,1}м\w{,3}|к\w{,1}т\w{,1}рый\s{,10}ч\w{,1}с)', s)
			if match:
				message = "Сейчас "+now.strftime("%H:%M")   # Вернет текущее время
			match = re.search(r'(?:к\w{,1}к\w{,1}й(?:\s{,10}|\s{,10}сейчас\s{,10})г\w{,1}д)|(?:к\w{,1}к\w{,1}ое\s{,10}ч\w{,1}сл\w{,1})', s)
			if match:
				message = now.strftime("%d.%m.%Y")  # Вернет текущую дату

			# шаблонное выражение для умножения
			match = re.search(r'(?:по|у)множ\w+\s{,10}(\d{1,10})\s{,10}(?:на|н\w{,1}|\w{,1}а|и)\s{,10}(\d{1,10})', s)
			if match:
				s1 = float(match[1])
				s2 = float(match[2])
				try:
					answer = s1 * s2
				except:
					message = "Неверный формат"
				message = str(answer)

			# шаблонное выражение для сложения
			match = re.search(r'(?:сложи|прибавь)\s{,10}(\d{1,10})\s{,10}(?:и|к)\s{,10}(\d{1,10})', s)
			if match:
				s1 = float(match[1])
				s2 = float(match[2])
				try:
					answer = s1 + s2
				except:
					message = "Неверный формат"
				message = str(answer)

			# шаблонное выражение для вычитания
			match = re.search(r'(?:вычти)\s{,10}(\d{1,10})\s{,10}(?:из)\s{,10}(\d{1,10})', s)
			if match:
				s1 = float(match[1])
				s2 = float(match[2])
				try:
					answer = s2 - s1
				except:
					message = "Неверный формат"
				message = str(answer)

			# шаблонное выражение для деления
			match = re.search(r'(?:раздели)\s{,10}(\d{1,10})\s{,10}(?:на)\s{,10}(\d{1,10})', s)
			if match:
				s1 = float(match[1])
				s2 = float(match[2])
				try:
					answer = s1 / s2
				except:
					message = "Неверный формат"
				message = str(answer)
			# Что есть смысл?
			match = re.search(r'(?:что есть смысл жизни|в чем смысл|в чем смысл жизни)', s)
			if match:
				message = "42"

			# шаблонное выражение для запроса погоды
			match = re.search(r'(?:к\w{,1}к\w{,1}я){,1}\s{,10}(?:с\w{,1}йч\w{,1}с){,1}\s{,10}(?:п\w{,1}года)', s)
			if match:
				message = self.find_out_weather()

			self.fill_dict(now.strftime("%d.%m.%Y %H:%M:%S"), [s, message])
			return message
