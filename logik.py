import sqlite3


class Logik:
    def __init__(self):

        self.conn = sqlite3.connect('testDB.db') #CONNECT TO DB
        self.cursor = self.conn.cursor()

        sql = "SELECT SUM(prise) from model WHERE free = 'no' and data = '01.02.2021' OR free = 'no' and data = '02.02.2021' OR free = 'no' and data = '03.02.2021' OR free = 'no' and data = '04.02.2021' OR free = 'no' and data = '05.02.2021' OR free = 'no' and data = '06.02.2021' OR free = 'no' and data = '07.02.2021'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        tmp = tmp[0]
        self.SEVENDAY_all_prise = tmp[0]

        sql = "SELECT SUM(prise) from model WHERE free = 'no' and data = '01.02.2021' OR free = 'no' and data = '02.02.2021' OR free = 'no' and data = '03.02.2021' OR free = 'no' and data = '04.02.2021' OR free = 'no' and data = '05.02.2021' OR free = 'no' and data = '06.02.2021' OR free = 'no' and data = '07.02.2021' OR free = 'no' and data = '08.02.2021' OR free = 'no' and data = '09.02.2021' OR free = 'no' and data = '10.02.2021'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        tmp = tmp[0]
        self.DECADA_all_prise = tmp[0]

        sql = "select sum(prise) from model where free = 'no'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        tmp = tmp[0]
        self.ALLPRISE_all_prise = tmp[0]

        sql = "SELECT SUM(prise) from model WHERE free = 'no' and data = '11.02.2021' OR free = 'no' and data = '12.02.2021' OR free = 'no' and data = '13.02.2021' OR free = 'no' and data = '14.02.2021' OR free = 'no' and data = '15.02.2021' OR free = 'no' and data = '16.02.2021' OR free = 'no' and data = '17.02.2021' OR free = 'no' and data = '18.02.2021' OR free = 'no' and data = '19.02.2021' OR free = 'no' and data = '20.02.2021'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        tmp = tmp[0]
        self.TWODECADA_all_prise = tmp[0]


        sql = "select free from model where data = '01.02.2021' OR data = '02.02.2021' OR data = '03.02.2021' OR data = '04.02.2021' OR data = '05.02.2021' OR data = '06.02.2021' OR data = '07.02.2021'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        self.n_SEVENDAY_COUNT = 0
        for row in tmp:

            if str(row[0][0]) == 'n':

                self.n_SEVENDAY_COUNT +=1
            else:

                pass


        sql = "select free from model where data = '01.02.2021' OR data = '02.02.2021' OR data = '03.02.2021' OR data = '04.02.2021' OR data = '05.02.2021' OR data = '06.02.2021' OR data = '07.02.2021' OR data = '08.02.2021' OR data = '09.02.2021' OR data = '10.02.2021'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        self.n_DECADA_COUNT = 0

        for row in tmp:

            if str(row[0][0]) == 'n':

                self.n_DECADA_COUNT +=1

            else:
                pass



        sql = "select free from model where data = '11.02.2021' OR data = '12.02.2021' OR data = '13.02.2021' OR data = '14.02.2021' OR data = '15.02.2021' OR data = '16.02.2021' OR data = '17.02.2021' OR data = '18.02.2021' OR data = '19.02.2021' OR data = '20.02.2021'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        self.n_TWODECADA_COUNT = 0

        for row in tmp:

            if str(row[0][0]) == 'n':
                self.n_TWODECADA_COUNT += 1

            else:

                pass


        sql = "select free from model"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()

        self.n_ALL_COUNT = 0

        for row in tmp:

            if str(row[0][0]) == 'n':
                self.n_ALL_COUNT += 1

            else:
                pass

        self.SEVENDAY_ADR = self.SEVENDAY_all_prise / self.n_SEVENDAY_COUNT
        self.DECADA_ADR = self.DECADA_all_prise / self.n_DECADA_COUNT
        self.TWODECADA_ADR = self.TWODECADA_all_prise / self.n_TWODECADA_COUNT
        self.ALL_ADR = self.ALLPRISE_all_prise / self.n_ALL_COUNT


        self.OCC_SEVEN_DAY = (self.n_SEVENDAY_COUNT / 70) * 100
        self.OCC_DECADA = (self.n_DECADA_COUNT / 100) * 100
        self.OCC_TWODACADA = (self.n_TWODECADA_COUNT / 100) * 100
        self.OCC_ALL = (self.n_ALL_COUNT / 280) * 100



        self.RP_SEVEN_DAY = (self.SEVENDAY_all_prise / 70)
        self.RP_DECADA = (self.DECADA_all_prise / 100)
        self.RP_TWODECADA = (self.TWODECADA_all_prise / 100)
        self.RP_ALL = (self.ALLPRISE_all_prise / 280)



        self.record()





    def record(self):

        self.MY_counter = 1
        sql = "UPDATE settings SET number = '" + str(self.SEVENDAY_ADR) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.DECADA_ADR) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.TWODECADA_ADR) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.ALL_ADR) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1


        sql = "UPDATE settings SET number = '" + str(self.OCC_SEVEN_DAY) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.OCC_DECADA) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.OCC_TWODACADA) + "' WHERE id = '" + str(
            self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.OCC_ALL) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1


        sql = "UPDATE settings SET number = '" + str(self.RP_SEVEN_DAY) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.RP_DECADA) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.RP_TWODECADA) + "' WHERE id = '" + str(
            self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1

        sql = "UPDATE settings SET number = '" + str(self.RP_ALL) + "' WHERE id = '" + str(self.MY_counter) + "' "
        self.cursor.execute(sql)
        self.conn.commit()
        self.MY_counter += 1











        






