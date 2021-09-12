class Change():
    def __init__(self, table, cursor, con):
        self.table = table
        self.cursor = cursor
        self.con = con

    def sett_update(self, num, nam, zna):
        sql = f"""
        UPDATE {self.table}
        SET {nam} = '{zna}'
        WHERE id = {num}"""
        self.cursor.execute(sql)
        self.con.commit()

    def appen(self, staff, column):
        column_r = ",".join(column)
        if type(staff) == tuple:
            print("tuple")
            self.cursor.execute(f"INSERT INTO {self.table}{column_r} VALUES {staff}")
        if type(staff) == list:
            staff_r = ",".join(staff)
            print("list")
            self.cursor.execute(f"INSERT INTO {self.table}{column_r} VALUES {staff_r}")
        self.con.commit()

    def delet(self, id_del):
        self.cursor.execute(f"DELETE FROM {self.table} WHERE id = '{id_del}'")
        self.con.commit()

    def delet_table(self):
        self.cursor.execute(f"DROP TABLE {self.table}")
        self.con.commit()

    def show(self) -> object:
        self.cursor.execute(f"SELECT * FROM {self.table}")
        for i in self.cursor.fetchall():
            print(i)