from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import  QMessageBox

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