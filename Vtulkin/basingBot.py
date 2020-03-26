
class AbstractBot:
    """ Абстрактный класс "чат-бот" """

    def find_out_weather(self) -> str:
        """ Запрос погоды """
        pass

    def get_history_of_chatting(self) -> dict:
        pass

    def write_to_json(self):
        """ Запись в файл"""
        pass

    def read_from_json(self):
        """ Чтение из файла с именем пользователя"""
        pass

    def fill_dict(self, key, data):
        """ ЗАполнить запись"""
        pass

    def set_name_of_user(self, name):
        """ задает имя пользователя и ищет подходящий файл с историей сообщений"""
        pass

    def __init__(self, user_name="user"):
        """ Конструктор для инициализации имени пользователя и истории сообщений"""
        pass

    def reply(self, s) -> str:
        """ Метод "ответа бота". Вернет строку с ответом. """
        pass
