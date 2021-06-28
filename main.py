import  psycopg2  # импорт библиотеки

con = psycopg2.connect(dbname='WorkBase', user='postgres',
                        password='14319', host='localhost')  # связь с базой данных  # связь с базой данных
cursor = con.cursor()  # создание обькта для взаимодействия с базой

class Change():
    def __init__(self, table):
        self.table = table

    def sett_update(self, num, nam, zna):
        sql = f"""
        UPDATE {self.table}
        SET {nam} = '{zna}'
        WHERE id = {num}"""
        cursor.execute(sql)
        con.commit()

    def appen(self, staff, column):
        column_r = ",".join(column)
        if type(staff) == tuple:
            print("tuple")
            cursor.execute(f"INSERT INTO {self.table}{column_r} VALUES {staff}")
        if type(staff) == list:
            staff_r = ",".join(staff)
            print("list")
            cursor.execute(f"INSERT INTO {self.table}{column_r} VALUES {staff_r}")
        con.commit()

    def delet(self, id_del):
        cursor.execute(f"DELETE FROM {self.table} WHERE id = '{id_del}'")
        con.commit()

    def delet_table(self):
        cursor.execute(f"DROP TABLE {self.table}")
        con.commit()


    def show(self):
        cursor.execute(f"SELECT * FROM {self.table}")
        for i in cursor.fetchall():
            print(i)


work_change = Change("staff")
work_change.show()
#work_change.sett_update(12, 'lastname', 'Gorin')
"""work_change.appen(["('Andrey', 'Gubin', 'Ivanovich', 40000, 'ingeneer'),"
             "('Ivan', 'Solomatin', 'Sergeevich', 38000, 'manager'),"
             "('Irina', 'Lobacheva', 'Sergeevna', 30000, 'operator'),"
             "('Lybin', 'Ilya', 'Petrovich', 60000, 'director')"],
                 ["(firstname, lastname, patronymic, salary, position)"] )"""











