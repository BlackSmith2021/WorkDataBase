import  psycopg2  # импорт библиотеки
from class_of_change import Change
dbname = None
user = None
password = None
host = None
d_from_property = {}

with open('AutrisingConfig.txt', 'r') as f:
    str_read = f.readlines()
    for find_str in str_read:  # перебор строк в файле
        if find_str.find("=") != -1:  # если строка содержит символ, обрабатываем ее
            key_find = find_str[:find_str.find("=") -1]  # записываем в переменную ключа строку до символа
            value_find = find_str[find_str.find("=") +2:find_str.find("/n")]  # записываем в переменную значния по ключу строку после символа
            d_from_property.update({key_find:value_find})  # обновляем словарь

print(d_from_property)

with open('AutrisingConfig.txt', 'r') as f:
    str_read = f.readlines()
    print(str_read)
    for i in str_read:
        if i.find("dbname") != (-1):
            dbname = i.split('=')[1].strip()
        elif i.find("user") != (-1):
            user = i.split('=')[1].strip()
        elif i.find("password") != (-1):
            password = i.split('=')[1].strip()
        elif i.find("host") != (-1):
            host = i.split('=')[1].strip()

if None not in (dbname, user, password, host):
    con = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host)  # связь с базой данных  # связь с базой данных
    cursor = con.cursor()  # создание обькта для взаимодействия с базой

    work_change = Change("staff", cursor, con)
    #work_change.show()
    #work_change.delet_table()
    #work_change.sett_update(12, 'lastname', 'Gorin')
    """work_change.appen(["('Andrey', 'Gubin', 'Ivanovich', 40000, 'ingeneer'),"
                 "('Ivan', 'Solomatin', 'Sergeevich', 38000, 'manager'),"
                 "('Irina', 'Lobacheva', 'Sergeevna', 30000, 'operator'),"
                 "('Lybin', 'Ilya', 'Petrovich', 60000, 'director')"],
                     ["(firstname, lastname, patronymic, salary, position)"])"""
    work_change.show()











