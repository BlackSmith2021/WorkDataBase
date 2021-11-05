import sys

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel  #импорт библиотек работы с SQL
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
)

def get_property(file='AutrisingConfig.txt'):  # функция упаковки пропертей в словарь
    d_from_property = {}
    with open(file, 'r') as f:
        str_read = f.readlines()
        for find_str in str_read:  # перебор строк в файле
            if find_str.find("=") != -1:  # если строка содержит символ, обрабатываем ее
                key_find = find_str[:find_str.find("=") - 1]  # записываем в переменную ключа строку до символа
                value_find = find_str[find_str.find("=") + 2:find_str.find(
                    "/n")]  # записываем в переменную значния по ключу строку после символа
                d_from_property.update({key_find: value_find})  # обновляем словарь
    return d_from_property


propertyes = get_property()
dbname = propertyes['dbname']
user = propertyes['user']
password = propertyes['password']
host = propertyes['host']

class Staff(QMainWindow):   # создание класса окна
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")   # название окна
        self.resize(415, 200)  # размер окена
        # Set up the model
        self.model = QSqlTableModel(self)  # создает редактируемый QSqlTableModel объект
        self.model.setTable("staff")  # связывает модель с таблицей в базе данных с помощью .setTable().
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # устанавливает стратегию редактирования модели OnFieldChange. Эта стратегия позволяет модели автоматически обновлять данные в вашей базе данных, если пользователь изменяет какие-либо данные непосредственно в представлении.
        self.model.setHeaderData(0, Qt.Horizontal, "ID")  # устанавливают несколько удобных меток для горизонтальных заголовков модели using .setHeaderData()
        self.model.setHeaderData(1, Qt.Horizontal, "firstName")
        self.model.setHeaderData(2, Qt.Horizontal, "lastName")
        self.model.setHeaderData(3, Qt.Horizontal, "patronymic")
        self.model.setHeaderData(3, Qt.Horizontal, "position_id")
        self.model.select()  # загружает данные из базы данных и заполняет модель путем вызова .select().
        # Set up the view
        self.view = QTableView()  # создает объект табличного представления для отображения данных, содержащихся в модели.
        self.view.setModel(self.model)  # связывает представление с моделью, вызывая .setModel() представление с моделью данных в качестве аргумента.
        self.view.resizeColumnsToContents()  # вызывает .resizeColumnsToContents() объект просмотра, чтобы настроить таблицу в соответствии с ее содержимым.
        self.setCentralWidget(self.view)  # запускает выджет


def createConnection():  # создание соединения с БД
    con = QSqlDatabase.addDatabase("QPSQL")
    con.setDatabaseName(dbname)
    con.setUserName(user)
    con.setPassword(password)
    con.setHostName(host)
    if not con.open():  # проверка на неудачное соединение
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
win = Staff()
win.show()
sys.exit(app.exec_())