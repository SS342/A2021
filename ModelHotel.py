import sqlite3
import tkinter as tk
import sqlite3
from logik import Logik

class ModelHotel:

    def __init__(self,tab,text,Button):

        self.tab = tab
        self.text = text
        self.button = Button

        self.counter1 = 1
        self.counter2 = 2
        self.counter3 = 3
        self.counter4 = 4
        self.counter5 = 5
        self.counter6 = 6
        self.counter7 = 7
        self.counter8 = 8
        self.counter9 = 9
        self.counter10 = 10

        self.text.destroy()
        self.button.destroy()

        self.root = tk.Tk()

        self.root.geometry('500x500')

        self.root.title('Model')

        self.data = 1

        if self.data < 10:

            self.myData = f"0{self.data}.02.2021"

        else:

            self.myData = f"{self.data}.02.2021"

        self.roomTXT1 = 'Номер - 1'
        self.roomTXT2 = 'Номер - 2'
        self.roomTXT3 = 'Номер - 3'
        self.roomTXT4 = 'Номер - 4'
        self.roomTXT5 = 'Номер - 5'
        self.roomTXT6 = 'Номер - 6'
        self.roomTXT7 = 'Номер - 7'
        self.roomTXT8 = 'Номер - 8'
        self.roomTXT9 = 'Номер - 9'
        self.roomTXT10 = 'Номер - 10'

        self.conn = sqlite3.connect('testDB.db')
        self.cursor = self.conn.cursor()

        self.myData1 = tk.Label(
            self.root,
            text = self.myData,
            font=(
                None,
                20
            )
        )

        self.myData1.place(
            x = 170,
            y = 0
        )



        self.roomTXT1 = tk.Label(
            self.root,
            text = self.roomTXT1,
            font=(
                None,
                15
            )
        )

        self.roomTXT1.place(
            x = 0,
            y = 40
        )

        self.roomTXT2 = tk.Label(
            self.root,
            text=self.roomTXT2,
            font=(
                None,
                15
            )
        )

        self.roomTXT2.place(
            x=0,
            y=80
        )

        self.roomTXT3 = tk.Label(
            self.root,
            text=self.roomTXT3,
            font=(
                None,
                15
            )
        )

        self.roomTXT3.place(
            x=0,
            y=120
        )

        self.roomTXT4 = tk.Label(
            self.root,
            text=self.roomTXT4,
            font=(
                None,
                15
            )
        )

        self.roomTXT4.place(
            x=0,
            y=160
        )

        self.roomTXT5 = tk.Label(
            self.root,
            text=self.roomTXT5,
            font=(
                None,
                15
            )
        )

        self.roomTXT5.place(
            x=0,
            y=200
        )

        self.roomTXT6 = tk.Label(
            self.root,
            text=self.roomTXT6,
            font=(
                None,
                15
            )
        )

        self.roomTXT6.place(
            x=0,
            y=240
        )

        self.roomTXT7 = tk.Label(
            self.root,
            text=self.roomTXT7,
            font=(
                None,
                15
            )
        )

        self.roomTXT7.place(
            x=0,
            y=280
        )

        self.roomTXT8 = tk.Label(
            self.root,
            text=self.roomTXT8,
            font=(
                None,
                15
            )
        )

        self.roomTXT8.place(
            x=0,
            y=320
        )

        self.roomTXT9 = tk.Label(
            self.root,
            text=self.roomTXT9,
            font=(
                None,
                15
            )
        )

        self.roomTXT9.place(
            x=0,
            y=360
        )
        self.roomTXT10 = tk.Label(
            self.root,
            text=self.roomTXT10,
            font=(
                None,
                15
            )
        )

        self.roomTXT10.place(
            x=0,
            y=400
        )

        # ENTRY

        self.room1Entry = tk.Entry(
            self.root,
            width = 25
        )

        self.room1Entry.place(
            x = 200,
            y = 40 + 5
        )

        self.room2Entry = tk.Entry(
            self.root,
            width=25
        )

        self.room2Entry.place(
            x=200,
            y=80 + 5
        )

        self.room3Entry = tk.Entry(
            self.root,
            width=25
        )

        self.room3Entry.place(
            x=200,
            y=120 + 5
        )

        self.room4Entry = tk.Entry(
            self.root,
            width=25
        )

        self.room4Entry.place(
            x=200,
            y=160 + 5
        )

        self.room5Entry = tk.Entry(
            self.root,
            width=25
        )
        self.room5Entry.place(
            x=200,
            y=200 + 5
        )

        self.room6Entry = tk.Entry(
            self.root,
            width=25
        )

        self.room6Entry.place(
            x=200,
            y=240 + 5
        )

        self.room7Entry = tk.Entry(
            self.root,
            width=25
        )

        self.room7Entry.place(
            x=200,
            y=280 + 5
        )

        self.room8Entry = tk.Entry(
            self.root,
            width=25
        )

        self.room8Entry.place(
            x=200,
            y=320 + 5
        )

        self.room9Entry = tk.Entry(
            self.root,
            width=25
        )
        self.room9Entry.place(
            x=200,
            y=360 + 5
        )

        self.room10Entry = tk.Entry(
            self.root,
            width=25
        )
        self.room10Entry.place(
            x=200,
            y=400 + 5
        )

         ######
        ## Button
         ######

        GeneralButton = tk.Button(
            self.root,
            width = 20,
            text = 'Дальше',
            background = "#DCDCDC",
            command = lambda: self.update()
        )

        GeneralButton.place(
            x = 200,
            y = 450
        )



    def update(self):

        self.data +=1
        first = self.room1Entry.get()
        second = self.room2Entry.get()
        third = self.room3Entry.get()

        fourth = self.room4Entry.get()
        fifth = self.room5Entry.get()
        sixth = self.room6Entry.get()

        seventh = self.room7Entry.get()
        eight = self.room8Entry.get()
        ninth = self.room9Entry.get()

        tenth = self.room10Entry.get()


        self.room1Entry.delete(
            0,
            last=tk.END
        )

        self.room2Entry.delete(
            0,
            last=tk.END
        )

        self.room3Entry.delete(
            0,
            last=tk.END
        )

        self.room4Entry.delete(
            0,
            last=tk.END
        )

        self.room5Entry.delete(
            0,
            last=tk.END
        )

        self.room6Entry.delete(
            0,
            last=tk.END
        )

        self.room7Entry.delete(
            0,
            last=tk.END
        )

        self.room8Entry.delete(
            0,
            last=tk.END
        )

        self.room9Entry.delete(
            0,
            last=tk.END
        )

        self.room10Entry.delete(
            0,
            last=tk.END
        )

        ########################################################UPDATE##################################################

        self.zero_prise = 0

        try:

            first = int(first)
            if first == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter1) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if first > 1850 and first < 7400:

                    sql = "UPDATE model SET prise = '" + str(first) + "'," " free= 'no' WHERE id = '" + str(self.counter1) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter1) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter1 +=10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter1) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter1 += 10

        try:

            second = int(second)
            if second == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(
                    self.counter2) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if second > 1850 and second < 7400:

                    sql = "UPDATE model SET prise = '" + str(second) + "'," " free= 'no' WHERE id = '" + str(
                        self.counter2) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter2) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter2 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter2) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter2 += 10

        try:

            third = int(third)
            if third == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter3) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if third > 1850 and third < 7400:

                    sql = "UPDATE model SET prise = '" + str(third) + "'," " free= 'no' WHERE id = '" + str(self.counter3) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter3) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter3 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter3) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter3 += 10


        try:

            fourth = int(fourth)
            if fourth == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter4) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if fourth > 1850 and fourth < 7400:

                    sql = "UPDATE model SET prise = '" + str(fourth) + "'," " free= 'no' WHERE id = '" + str(self.counter4) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter4) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter4 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter4) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter4 += 10


        try:

            fifth = int(fifth)
            if fifth == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter5) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if fifth > 1850 and fifth < 7400:

                    sql = "UPDATE model SET prise = '" + str(fifth) + "'," " free= 'no' WHERE id = '" + str(self.counter5) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter5) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter5 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter5) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter5 += 10


        try:

            sixth = int(sixth)
            if sixth == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter6) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if sixth > 1850 and sixth < 7400:

                    sql = "UPDATE model SET prise = '" + str(sixth) + "'," " free= 'no' WHERE id = '" + str(self.counter6) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter6) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter6 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter6) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter6 += 10


        try:

            seventh = int(seventh)
            if seventh == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter7) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if seventh > 1850 and seventh < 7400:

                    sql = "UPDATE model SET prise = '" + str(seventh) + "'," " free= 'no' WHERE id = '" + str(self.counter7) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter7) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter7 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter7) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter7 += 10

        try:

            eight = int(eight)
            if eight == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter8) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if eight > 1850 and eight < 7400:

                    sql = "UPDATE model SET prise = '" + str(eight) + "'," " free= 'no' WHERE id = '" + str(self.counter8) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter8) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter8 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter8) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter8 += 10

        try:

            ninth = int(ninth)
            if ninth == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter9) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if ninth > 1850 and ninth < 7400:

                    sql = "UPDATE model SET prise = '" + str(ninth) + "'," " free= 'no' WHERE id = '" + str(self.counter9) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter9) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter9 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter9) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter9 += 10

        try:

            tenth = int(tenth)
            if tenth == 0:

                sql = "UPDATE model SET prise = '" + str(self.zero_prise) + "'," " free= 'yes' WHERE id = '" + str(self.counter10) + "' "
                self.cursor.execute(sql)
                self.conn.commit()

            else:

                if tenth > 1850 and tenth < 7400:

                    sql = "UPDATE model SET prise = '" + str(tenth) + "'," " free= 'no' WHERE id = '" + str(self.counter10) + "' "
                    self.cursor.execute(sql)
                    self.conn.commit()

                else:

                    sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter10) + "'"
                    self.cursor.execute(sql)
                    self.conn.commit()

            self.counter10 += 10

        except:

            sql = "UPDATE model SET prise = '3700', free= 'no' WHERE id = '" + str(self.counter10) + "'"
            self.cursor.execute(sql)
            self.conn.commit()

            self.counter10 += 10






        ########################################################UPDATE##################################################
        if self.data < 10:

            self.myData = f"0{self.data}.02.2021"

            self.myData1 = tk.Label(
                self.root,
                text=self.myData,
                font=(
                    None,
                    20
                )
            )

            self.myData1.place(
                x=170,
                y=0
            )



        else:

            self.myData = f"{self.data}.02.2021"

            self.myData1 = tk.Label(
                self.root,
                text=self.myData,
                font=(
                    None,
                    20
                )
            )

            self.myData1.place(
                x=170,
                y=0
            )

        if self.data > 28:

            self.root.destroy()


            Logik()


            self.listbox = tk.Listbox(
                self.tab,
                width=195,
                height=40
            )

            self.sb = tk.Scrollbar(
                self.tab,
                orient=tk.HORIZONTAL
            )

            self.listbox.pack()
            self.sb.pack(
                fill=tk.X
            )

            self.listbox.configure(xscrollcommand=self.sb.set)
            self.sb.config(command=self.listbox.xview)

            self.str1 = 'Дата                  01.02.2021    02.02.2021    03.02.2021    04.02.2021    05.02.2021    06.02.2021    07.02.2021    08.02.2021    09.02.2021    10.02.2021    11.02.2021    12.02.2021    13.02.2021    14.02.2021    15.02.2021    16.02.2021    17.02.2021    18.02.2021    19.02.2021    20.02.2021    21.02.2021    22.02.2021    23.02.2021    24.02.2021    25.02.2021    26.02.2021    27.02.2021    28.02.2021'
            self.str2 = 'номер - 1             '
            self.str3 = 'номер - 2             '
            self.str4 = 'номер - 3             '
            self.str5 = 'номер - 4             '
            self.str6 = 'номер - 5             '
            self.str7 = 'номер - 6             '
            self.str8 = 'номер - 7             '
            self.str9 = 'номер - 8             '
            self.str10 = 'номер - 9             '
            self.str11 = 'номер- 10            '
            self.listbox.insert(0,self.str1)



            self.taab_5 = '     '
            self.taab_4 = '    '
            self.taab_3 = '   '

            sql = "select prise from model where number = '1'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()

            for row in tmp:

                temp = row[0]

                temp = str(temp)

                if len(temp) ==1:

                    self.str2 = self.str2 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str2 = self.str2 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(1,self.str2)

            sql = "select prise from model where number = '2'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()

            for row in tmp:

                temp = row[0]
                print(temp)

                if len(temp) == 1:

                    self.str3 = self.str3 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str3 = self.str3 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(2, self.str3)

            sql = "select prise from model where number = '3'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()

            for row in tmp:
                temp = row[0]

                temp = str(temp)
                if len(temp) == 1:

                    self.str4 = self.str4 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str4 = self.str4 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '

            self.listbox.insert(3, self.str4)

            sql = "select prise from model where number = '4'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()
            for row in tmp:
                temp = row[0]
                print(temp)
                temp = str(temp)
                if len(temp) == 1:

                    self.str5 = self.str5 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str5 = self.str5 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(4, self.str5)

            sql = "select prise from model where number = '5'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()
            for row in tmp:

                temp = row[0]

                temp = str(temp)

                if len(temp) == 1:

                    self.str6 = self.str6 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str6 = self.str6 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(5, self.str6)

            sql = "select prise from model where number = '6'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()

            for row in tmp:

                temp = row[0]

                temp = str(temp)

                if len(temp) == 1:

                    self.str7 = self.str7 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str7 = self.str7 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(6, self.str7)

            sql = "select prise from model where number = '7'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()
            for row in tmp:

                temp = row[0]

                temp = str(temp)
                if len(temp) == 1:

                    self.str8 = self.str8 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:
                    self.str8 = self.str8 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(7, self.str8)

            sql = "select prise from model where number = '8'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()
            for row in tmp:
                temp = row[0]

                temp = str(temp)

                if len(temp) == 1:

                    self.str9 = self.str9 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str9 = self.str9 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(8, self.str9)

            sql = "select prise from model where number = '9'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()
            for row in tmp:

                temp = row[0]

                temp = str(temp)

                if len(temp) == 1:

                    self.str10 = self.str10 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str10 = self.str10 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(9, self.str10)

            sql = "select prise from model where number = '10'"
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()

            for row in tmp:

                temp = row[0]

                temp = str(temp)

                if len(temp) == 1:

                    self.str11 = self.str11 + self.taab_5 + temp + self.taab_4 + self.taab_5 + '      '

                else:

                    self.str11 = self.str11 + self.taab_3 + temp + self.taab_3 + self.taab_5 + '   '


            self.listbox.insert(10, self.str11)



