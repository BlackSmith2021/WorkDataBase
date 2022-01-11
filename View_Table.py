import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView,
)

from connecting import createConnection  # импорт функции коннекта с бд


class View_Table(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(415, 200)
        self.model = QSqlRelationalTableModel()  # создание обьекта QSqlRelationalTableModel для установки связи между
        # таблицами и подмены в представлении значения формируемой таблицы значениями из связных таблиц.
        self.view = QTableView()  # создание обьекта для заполнения и отбражения данных в таблице
        self.view.setModel(self.get_table_staff())
        self.view.setItemDelegate(QSqlRelationalDelegate(self.view))  # QSqlRelationalDelegate предоставляет поле
        # со списком для полей, которые являются внешними ключами в других таблицах
        self.view.resizeColumnsToContents()  # подстройка размера окна под отбражаемый контент
        self.setCentralWidget(self.view)

    def get_table_staff(self):
        self.model.setTable("staff")  # соединение с таблицей
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # выбор стратегии заполнения
        # задание условий соединения для столбцов 4, 5, 6 со звязанными таблицами
        self.model.setRelation(4, QSqlRelation("positions", "position_id", "name"))
        self.model.setRelation(5, QSqlRelation("salary", "salary_id", "salary"))
        self.model.setRelation(6, QSqlRelation("room_number", "room_id", "room"))
        # задание имен для отображаемых столбцов
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Lastname")
        self.model.setHeaderData(3, Qt.Horizontal, "Patronymic")
        self.model.setHeaderData(4, Qt.Horizontal, "Position")
        self.model.setHeaderData(5, Qt.Horizontal, "Salary")
        self.model.setHeaderData(6, Qt.Horizontal, "Room")
        self.model.select()
        return self.model


app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
win = View_Table()
win.show()
sys.exit(app.exec_())
