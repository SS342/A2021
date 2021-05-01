import sqlite3

class DataBase:

    def __init__(self):

        self.conn = sqlite3.connect('testDB.db')
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("""CREATE TABLE IF NOT EXISTS user(
                    ID   STRING,
                    name STRING,
                    middle_name STRING,
                    surname STRING,
                    number STRING);
                """)
        self.conn.commit()

        self.cursor1.execute("""CREATE TABLE IF NOT EXISTS user_OTVET( 
                            ID   STRING,
                            name STRING,
                            middle_name STRING,
                            surname STRING,
                            number STRING,
                            data STRING,
                            balls STRING,
                            mark STRING);
                        """)
        self.conn.commit()

        self.cursor1.execute("""CREATE TABLE IF NOT EXISTS model(
                                    ID   STRING,
                                    number STRING,
                                    prise STRING,
                                    free STRING,
                                    data STRING);
                                """)

        self.cursor1.execute("""CREATE TABLE IF NOT EXISTS settings(
                                    ID   STRING,
                                    number STRING);
                                """)
        self.conn.commit()
        sql = "select * from user where name = '8496' AND surname = '9203'"
        self.cursor1.execute(sql)
        tmp = self.cursor1.fetchall()
        if tmp:
            pass
        else:
            id = -1
            name = 8496
            midlle_name = 1282
            surname = 9203
            num = 0000
            sql = "insert into user values ('" + str(id) + "','" + str(name) + "','" + str(midlle_name) + "','" + str(
                surname) + "','" + str(num) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()

        self.model()

        self.Settngs()



    def model(self):

        data = 1
        number = 1
        price = '3700'
        free = 'no'
        id = 1

        sql = "SELECT * FROM model"

        self.cursor1.execute(sql)

        tmp = self.cursor1.fetchall()

        if tmp:

            pass

        else:

            for i in range(28):

                if data < 10:

                    mydata = f'0{data}.02.2021'

                else:

                    mydata = f'{data}.02.2021'

                for i in range(10):

                    self.cursor1.execute("insert into model values ('" + str(id) + "','" + str(number) + "','" + str(price) + "','" + str(free) + "','" + str(mydata) + "')")
                    self.conn.commit()

                    number += 1
                    id += 1

                number = 1
                data += 1


    def Settngs(self):

        sql = "SELECT * FROM settings"

        self.cursor1.execute(sql)

        tmp = self.cursor1.fetchall()

        if tmp:

            pass

        else:
            self.my_id = 1
            self.my_tmp = 123
            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1

            sql = "insert into settings values ('" + str(self.my_id) + "','" + str(self.my_tmp) + "')"
            self.cursor1.execute(sql)
            self.conn.commit()
            self.my_id += 1


    @staticmethod
    def student(name, midlle_name, surname, num):

        sql = "SELECT * FROM user WHERE name ='" + str(name) + "' AND middle_name = '" + str(midlle_name) + "' AND surname ='" + str(surname) + "' AND number = '" + str(num) + "' "
        conn = sqlite3.connect('testDB.db')
        cursor1 = conn.cursor()
        cursor1.execute(sql)
        tmp = cursor1.fetchall()

        if tmp:

            pass

        else:

            sql = "SELECT ID from user"
            cursor1.execute(sql)
            for row in cursor1.fetchall():

                tmp = row

            id = int(tmp[-1]) + 1
            sql = "insert into user values ('" + str(id) + "','" + str(name) + "','" + str(midlle_name) + "','" + str(surname) + "','" + str(num) + "')"
            cursor1.execute(sql)
            conn.commit()

DB = DataBase()
DB.model()


