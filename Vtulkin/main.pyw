from bot import Bot
import sys
import os
from PyQt5 import QtWidgets, QtCore
import form_main
import form_authorization


class Main(QtWidgets.QMainWindow, form_main.Ui_Form_main):
    """ класс главного окна"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._name_of_user = "user"  # имя пользователя, которое нужно передать боту
        self._bot = Bot(self._name_of_user)
        self.pushButton_enter.clicked.connect(self.get_message)
        # self.lineEdit_message.editingFinished.connect(self.get_message)  # дублируется при нажатии на pushButton_enter

    def closeEvent(self, evnt):
        self._bot.write_to_json()
        # super(Main, self).closeEvent(evnt)  # не совсем понимаю зачем \(o_o)/
        self.close()

    def get_message(self):
        s = self.lineEdit_message.text()
        self.lineEdit_message.setText("")
        self.textEdit.insertHtml("<div><font color=\"MediumVioletRed\">Вы: " + s + "<br></font></div>");
        self.textEdit.insertHtml("<div><font color=\"DarkBlue\">Бот: " + self._bot.reply(s) + "<br></font></div>");

    def get_name_of_user(self, name):
        """ метод задает имя пользователя и воссоздает разговор по истории(если она есть)"""
        if isinstance(name, str):
            self._name_of_user = name
            self._bot.set_name_of_user(name)
            rec = self._bot.get_history_of_chatting()
            if rec != {}:
                for key in rec.keys():
                    # self.textEdit.append("Вы: " + rec[key][0])
                    # self.textEdit.append("Бот: " + rec[key][1])
                    self.textEdit.insertHtml("<div><font color=\"MediumVioletRed\">Вы: " + rec[key][0] + "<br></font></div>");
                    self.textEdit.insertHtml(
                        "<div><font color=\"DarkBlue\">Бот: " + rec[key][1] + "<br></font></div>");


class StartWindow(QtWidgets.QMainWindow, form_authorization.Ui_Form_authorization):
    """ класс начального окна"""
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self._main = main_window  # ссылка на главную форму, чтобы ее открыть
        self.pushButton.clicked.connect(self.push_btn_enter)

    def push_btn_enter(self):
        if self.lineEdit_name.text() != "":
            self._main.get_name_of_user(self.lineEdit_name.text())
            self._main.show()
            self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main()  # Главное окно
    start_window = StartWindow(main_window)  # Начальное окно
    start_window.show()

    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
