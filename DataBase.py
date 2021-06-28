import  psycopg2
from psycopg2 import sql


con = psycopg2.connect(dbname='WorkBase', user='postgres',
                        password='14319', host='localhost')  # связь с базой данных
cursor = con.cursor()  # создание обькта для взаимодействия с базой

# создание таблицы
cursor.execute("""CREATE TABLE if NOT EXISTS staff 
               ( id SERIAL PRIMARY KEY, 
               firstname TEXT NOT NULL, 
               lastname TEXT NOT NULL, 
               patronymic TEXT NOT NULL, 
               salary INTEGER, 
               position TEXT NOT NULL)""")

con.commit()  # сохраняем изменения

# создание записи для добавления

staff_r = ",".join(["('Andrey', 'Gubin', 'Ivanovich', 40000, 'ingeneer'),"
                     "('Ivan', 'Solomatin', 'Sergeevich', 38000, 'manager'),"
                     "('Irina', 'Lobacheva', 'Sergeevna', 30000, 'operator'),"
                     "('Lybin', 'Ilya', 'Petrovich', 60000, 'director')"])
print(staff_r)
con.autocommit = True
# добавляем значения staff в таблицу, используя безопасный метод "?"
downl = (f"INSERT INTO staff(firstname, lastname, patronymic, salary, position) VALUES {staff_r}")

cursor.execute(downl)
con.commit()