
class AbstractBot:
    """ Абстрактный класс "чат-бот" """

    def __init__(self, user_name="user"):
        """ Конструктор для инициализации имени пользователя и истории сообщений"""
        pass

    def reply(self, s) -> str:
        """ Метод "ответа бота". Вернет строку с ответом. """
        pass
