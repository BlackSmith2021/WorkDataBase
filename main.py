import psycopg2  # импорт библиотеки
from class_of_change import Change

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

if None not in (dbname, user, password, host):
    con = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)  # связь с базой данных
    cursor = con.cursor()  # создание обькта для взаимодействия с базой

    work_change = Change("positions", cursor, con)
    # work_change.show()
    # work_change.delet_table()
    # work_change.sett_update(12, 'lastname', 'Gorin')
    """work_change.appen(["('Andrey', 'Gubin', 'Ivanovich', 40000, 'ingeneer'),"
                 "('Ivan', 'Solomatin', 'Sergeevich', 38000, 'manager'),"
                 "('Irina', 'Lobacheva', 'Sergeevna', 30000, 'operator'),"
                 "('Lybin', 'Ilya', 'Petrovich', 60000, 'director')"],
                     ["(firstname, lastname, patronymic, salary, position)"])"""
    work_change.show()
