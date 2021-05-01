import tkinter as tk
import sqlite3
from tkinter import messagebox
from workinex import Writer

class Functions:

    def __init__(self, name, midlle_name, surname, num):
        self.num = 0
        self.balls = 0

        self.conn = sqlite3.connect('testDB.db')
        self.cursor = self.conn.cursor()

        #Writer = Writer()
        Writer.stud()

        self.name = name
        self.midlle_name = midlle_name
        self.surname = surname
        self.num_user = num

    def TASK18(self):

        if str(self.entry12.get()) == str(2800):

            self.balls +=1


        self.TEXTT17.destroy()
        self.GENERAKTASK18.destroy()
        self.entry12.destroy()
        self.but.destroy()

        messagebox.showinfo("Результат", f"вы набрали {self.balls} балов")

        Writer.wirite(self.name, self.midlle_name, self.surname, self.num_user, self.balls)

    def TASK17(self):

        if str(self.entry11.get()) == str(35):

            self.balls += 1

        self.TEXTT16.destroy()
        self.GENERAKTASK17.destroy()
        self.entry11.destroy()

        self.TEXTT17 = tk.Label(
            self.root,
            text=self.TEXT[17],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK18 = tk.Label(
            self.root,
            text=self.GTASK[17],
            font=(
                None,
                20
            )
        )

        self.entry12 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT17.pack(side=tk.TOP)
        self.GENERAKTASK18.pack()
        self.entry12.pack()

    def TASK16(self):

        if str(self.entry10.get()) == str(7425000):

            self.balls += 1

        self.TEXTT15.destroy()
        self.GENERAKTASK16.destroy()
        self.entry10.destroy()

        self.TEXTT16 = tk.Label(
            self.root,
            text=self.TEXT[16],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK17 = tk.Label(
            self.root,
            text=self.GTASK[16],
            font=(
                None,
                20
            )
        )

        self.entry11 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT16.pack(side=tk.TOP)
        self.GENERAKTASK17.pack()
        self.entry11.pack()

    def TASK15(self):

        if str(self.entry9.get()) == str(19):

            self.balls += 1

        self.TEXTT14.destroy()
        self.GENERAKTASK15.destroy()
        self.entry9.destroy()

        self.TEXTT15 = tk.Label(
            self.root,
            text=self.TEXT[15],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK16 = tk.Label(
            self.root,
            text=self.GTASK[15],
            font=(
                None,
                20
            )
        )

        self.entry10 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT15.pack(side=tk.TOP)
        self.GENERAKTASK16.pack()
        self.entry10.pack()

    def TASK14(self):

        if str(self.entry8.get()) == str(1200):

            self.balls += 1

        self.TEXTT13.destroy()
        self.GENERAKTASK14.destroy()
        self.entry8.destroy()

        self.TEXTT14 = tk.Label(
            self.root,
            text=self.TEXT[14],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK15 = tk.Label(
            self.root,
            text=self.GTASK[14],
            font=(
                None,
                20
            )
        )

        self.entry9 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT14.pack(side=tk.TOP)
        self.GENERAKTASK15.pack()
        self.entry9.pack()

    def TASK13(self):

        if str(self.entry7.get()) == str(66.7):

            self.balls += 1

        self.TEXTT12.destroy()
        self.GENERAKTASK13.destroy()
        self.entry7.destroy()

        self.TEXTT13 = tk.Label(
            self.root,
            text=self.TEXT[13],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK14 = tk.Label(
            self.root,
            text=self.GTASK[13],
            font=(
                None,
                20
            )
        )

        self.entry8 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT13.pack(side=tk.TOP)
        self.GENERAKTASK14.pack()
        self.entry8.pack()

    def TASK12(self):

        if str(self.entry6.get()) == str(4500):

            self.balls += 1

        self.TEXTT11.destroy()
        self.GENERAKTASK12.destroy()
        self.entry6.destroy()

        self.TEXTT12 = tk.Label(
            self.root,
            text=self.TEXT[12],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK13 = tk.Label(
            self.root,
            text=self.GTASK[12],
            font=(
                None,
                20
            )
        )

        self.entry7 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT12.pack(side=tk.TOP)
        self.GENERAKTASK13.pack()
        self.entry7.pack()

    def TASK11(self):

        if str(self.entry5.get()) == str(42):

            self.balls += 1

        self.TEXTT10.destroy()
        self.GENERAKTASK11.destroy()
        self.entry5.destroy()

        self.TEXTT11 = tk.Label(
            self.root,
            text=self.TEXT[11],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK12 = tk.Label(
            self.root,
            text=self.GTASK[11],
            font=(
                None,
                20
            )
        )

        self.entry6 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT11.pack(side=tk.TOP)
        self.GENERAKTASK12.pack()
        self.entry6.pack()



    def TASK10(self):

        if str(self.entry4.get()) == str(4030000):

            self.balls += 1

        self.TEXTT9.destroy()
        self.GENERAKTASK10.destroy()
        self.entry4.destroy()

        self.TEXTT10 = tk.Label(
            self.root,
            text=self.TEXT[10],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK11 = tk.Label(
            self.root,
            text=self.GTASK[10],
            font=(
                None,
                20
            )
        )

        self.entry5 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT10.pack(side=tk.TOP)
        self.GENERAKTASK11.pack()
        self.entry5.pack()

    def TASK9(self):

        sql = "SELECT number FROM settings WHERE id = 11"
        self.cursor.execute(sql)

        tmp = self.cursor.fetchall()[-1][-1]

        if str(self.entry3.get()) == str(round(tmp, 2)):

            self.balls += 1

        self.TEXTT8.destroy()
        self.GENERAKTASK9.destroy()
        self.entry3.destroy()

        self.TEXTT9 = tk.Label(
            self.root,
            text=self.TEXT[9],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK10 = tk.Label(
            self.root,
            text=self.GTASK[9],
            font=(
                None,
                20
            )
        )

        self.entry4 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT9.pack(side=tk.TOP)
        self.GENERAKTASK10.pack()
        self.entry4.pack()

    def TASK8(self):

        sql = "SELECT number FROM settings WHERE id = 7"
        self.cursor.execute(sql)

        tmp = self.cursor.fetchall()[-1][-1]

        if str(self.entry2.get()) == str(round(tmp, 2)):

            self.balls += 1

        self.GENERAKTASK8.destroy()
        self.TEXTT7.destroy()
        self.entry2.destroy()
        self.TEXTT8 = tk.Label(
            self.root,
            text=self.TEXT[8],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK9 = tk.Label(
            self.root,
            text=self.GTASK[8],
            font=(
                None,
                20
            )
        )

        self.entry3 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT8.pack(side=tk.TOP)
        self.GENERAKTASK9.pack()
        self.entry3.pack()

    def TASK7(self):

        sql = "SELECT number FROM settings WHERE id = 3"
        self.cursor.execute(sql)

        tmp = self.cursor.fetchall()[-1][-1]

        if str(self.entry1.get()) == str(round(tmp,2)):

            self.balls += 1

        self.GENERAKTASK7.destroy()
        self.TEXTT6.destroy()
        self.entry1.destroy()
        self.TEXTT7 = tk.Label(
            self.root,
            text=self.TEXT[7],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK8 = tk.Label(
            self.root,
            text=self.GTASK[7],
            font=(
                None,
                20
            )
        )

        self.entry2 = tk.Entry(
            self.root,
            width=25
        )

        self.TEXTT7.pack(side=tk.TOP)
        self.GENERAKTASK8.pack()
        self.entry2.pack()

    def TASK6(self):

        if int(self.group_6.get()) == 4:

            self.balls += 1

        self.TEXTT5.destroy()
        self.BUT41.destroy()
        self.BUT42.destroy()
        self.BUT43.destroy()
        self.BUT44.destroy()
        self.BUT45.destroy()
        self.GENERAKTASK6.destroy()

        self.TEXTT6 = tk.Label(
            self.root,
            text=self.TEXT[6],
            font=(
                None,
                10
            )
        )

        self.GENERAKTASK7 = tk.Label(
            self.root,
            text=self.GTASK[6],
            font=(
                None,
                20
            )
        )

        self.entry1 = tk.Entry(
            self.root,
            width = 25
        )

        self.TEXTT6.pack(side=tk.TOP)
        self.GENERAKTASK7.pack()
        self.entry1.pack()


    def TASK5(self):

        if int(self.group_5.get()) == 4:

            self.balls += 1

        self.TEXTT4.destroy()
        self.BUT31.destroy()
        self.BUT32.destroy()
        self.BUT33.destroy()
        self.BUT34.destroy()
        self.BUT35.destroy()
        self.GENERAKTASK5.destroy()

        self.TEXTT5 = tk.Label(
            self.root,
            text=self.TEXT[5],
            font=(
                None,
                10
            )
        )

        self.group_6 = tk.IntVar()
        self.BUT41 = tk.Radiobutton(
            self.root,
            text='ARD',
            value=1,
            variable=self.group_6
        )

        self.BUT42 = tk.Radiobutton(
            self.root,
            text='PaRev',
            value=2,
            variable=self.group_6
        )

        self.BUT43 = tk.Radiobutton(
            self.root,
            text='RevPar',
            value=3,
            variable=self.group_6
        )

        self.BUT44 = tk.Radiobutton(
            self.root,
            text='Occupancy',
            value=4,
            variable=self.group_6
        )

        self.BUT45 = tk.Radiobutton(
            self.root,
            text='ADR',
            value=5,
            variable=self.group_6
        )

        self.GENERAKTASK6 = tk.Label(
            self.root,
            text=self.GTASK[5],
            font=(
                None,
                20
            )
        )

        self.TEXTT5.pack(side=tk.TOP)
        self.GENERAKTASK6.pack()
        self.BUT41.pack()
        self.BUT42.pack()
        self.BUT43.pack()
        self.BUT44.pack()
        self.BUT45.pack()

    def TASK4(self):

        if int(self.group_4.get()) == 5:

            self.balls += 1

        self.TEXTT3.destroy()
        self.BUT21.destroy()
        self.BUT22.destroy()
        self.BUT23.destroy()
        self.BUT24.destroy()
        self.BUT25.destroy()
        self.GENERAKTASK4.destroy()

        self.TEXTT4 = tk.Label(
            self.root,
            text=self.TEXT[4],
            font=(
                None,
                10
            )
        )

        self.group_5 = tk.IntVar()
        self.BUT31 = tk.Radiobutton(
            self.root,
            text='ARD',
            value=1,
            variable=self.group_5
        )

        self.BUT32 = tk.Radiobutton(
            self.root,
            text='PaRev',
            value=2,
            variable=self.group_5
        )

        self.BUT33 = tk.Radiobutton(
            self.root,
            text='RevPar',
            value=3,
            variable=self.group_5
        )

        self.BUT34 = tk.Radiobutton(
            self.root,
            text='Occupancy',
            value=4,
            variable=self.group_5
        )

        self.BUT35 = tk.Radiobutton(
            self.root,
            text='ADR',
            value=5,
            variable=self.group_5
        )

        self.GENERAKTASK5 = tk.Label(
            self.root,
            text=self.GTASK[4],
            font=(
                None,
                20
            )
        )

        self.TEXTT4.pack(side=tk.TOP)
        self.GENERAKTASK5.pack()
        self.BUT31.pack()
        self.BUT32.pack()
        self.BUT33.pack()
        self.BUT34.pack()
        self.BUT35.pack()


    def TASK3(self):

        if int(self.group_3.get()) == 3:

            self.balls += 1

        self.TEXTT2.destroy()
        self.BUT11.destroy()
        self.BUT12.destroy()
        self.BUT13.destroy()
        self.BUT14.destroy()
        self.BUT15.destroy()
        self.GENERAKTASK3.destroy()

        self.TEXTT3 = tk.Label(
            self.root,
            text=self.TEXT[3],
            font=(
                None,
                10
            )
        )

        self.group_4 = tk.IntVar()
        self.BUT21 = tk.Radiobutton(
            self.root,
            text='ARD',
            value=1,
            variable=self.group_4
        )

        self.BUT22 = tk.Radiobutton(
            self.root,
            text='PaRev',
            value=2,
            variable=self.group_4
        )

        self.BUT23 = tk.Radiobutton(
            self.root,
            text='RevPar',
            value=3,
            variable=self.group_4
        )

        self.BUT24 = tk.Radiobutton(
            self.root,
            text='Occupancy',
            value=4,
            variable=self.group_4
        )


        self.BUT25 = tk.Radiobutton(
            self.root,
            text='ADR',
            value=5,
            variable=self.group_4
        )

        self.GENERAKTASK4 = tk.Label(
            self.root,
            text=self.GTASK[3],
            font=(
                None,
                20
            )
        )

        self.TEXTT3.pack(side=tk.TOP)
        self.GENERAKTASK4.pack()
        self.BUT21.pack()
        self.BUT22.pack()
        self.BUT23.pack()
        self.BUT24.pack()
        self.BUT25.pack()

    def TASK2(self):

        if int(self.group_2.get()) == 4:

            self.balls += 1

        self.TEXTT1.destroy()
        self.BUT1.destroy()
        self.BUT2.destroy()
        self.BUT3.destroy()
        self.BUT4.destroy()
        self.BUT5.destroy()
        self.GENERAKTASK2.destroy()

        self.TEXTT2 = tk.Label(
            self.root,
            text=self.TEXT[2],
            font=(
                None,
                10
            )
        )

        self.group_3 = tk.IntVar()

        self.BUT11 = tk.Radiobutton(
            self.root,
            text='ARD',
            value=1,
            variable=self.group_3
        )

        self.BUT12 = tk.Radiobutton(
            self.root,
            text='PaRev',
            value=2,
            variable=self.group_3
        )

        self.BUT13 = tk.Radiobutton(
            self.root,
            text='RevPar',
            value=3,
            variable=self.group_3
        )

        self.BUT14 = tk.Radiobutton(
            self.root,
            text='Occupancy',
            value=4,
            variable=self.group_3
        )

        self.BUT15 = tk.Radiobutton(
            self.root,
            text='ADR',
            value=5,
            variable=self.group_3
        )

        self.GENERAKTASK3 = tk.Label(
            self.root,
            text=self.GTASK[2],
            font=(
                None,
                20
            )
        )

        self.TEXTT2.pack(side = tk.TOP)
        self.GENERAKTASK3.pack()
        self.BUT11.pack()
        self.BUT12.pack()
        self.BUT13.pack()
        self.BUT14.pack()
        self.BUT15.pack()

    def TASK1(self,otvet):

        if int(otvet) == 3:

            self.balls += 1

        self.rad[0].destroy()
        self.rad[1].destroy()
        self.rad[2].destroy()
        self.rad[3].destroy()
        self.rad[4].destroy()
        self.txt1.destroy()
        self.txt.destroy()

        self.TEXTT1 = tk.Label(
            self.root,
            text = self.TEXT[1],
            font=(
                None,
                10
            )
        )

        self.group_2 = tk.IntVar()


        self.BUT1 = tk.Radiobutton(
            self.root,
            text='ARD',
            value=1,
            variable=self.group_2
        )

        self.BUT2 = tk.Radiobutton(
            self.root,
            text='PaRev',
            value=2,
            variable=self.group_2
        )

        self.BUT3 = tk.Radiobutton(
            self.root,
            text='RevPar',
            value=3,
            variable=self.group_2
        )

        self.BUT4 = tk.Radiobutton(
            self.root,
            text='Occupancy',
            value=4,
            variable=self.group_2
        )

        self.BUT5 = tk.Radiobutton(
            self.root,
            text='ADR',
            value=5,
            variable=self.group_2
        )

        self.GENERAKTASK2 = tk.Label(
            self.root,
            text = self.GTASK[1],
            font=(
                None,
                20
            )
        )

        self.TEXTT1.pack(side=tk.TOP)
        self.GENERAKTASK2.pack()

        self.BUT1.pack()
        self.BUT2.pack()
        self.BUT3.pack()
        self.BUT4.pack()
        self.BUT5.pack()



    def TASK(self, txt, wind, TASK, TEXT, txt1, RAD, otvet,but):

        self.txt = txt
        self.root = wind
        self.GTASK = TASK
        self.TEXT = TEXT
        self.txt1 = txt1
        self.rad = RAD
        self.otvet = otvet
        self.but = but

        if int(self.num) == 0:

            messagebox.showinfo("Заполнение", "В заданиях 1 - 6 вам нужно выбрать правильный ответ.\nВ заданиях 7 - 18 нужно записать ответ.\nПример написания ответа: 3.14")
            self.num +=1

        elif int(self.num) == 1:

            self.TASK1(self.otvet)
            self.num += 1

        elif int(self.num) == 2:

            self.TASK2()
            self.num += 1

        elif int(self.num) == 3:

            self.TASK3()
            self.num += 1

        elif int(self.num) == 4:

            self.TASK4()
            self.num += 1

        elif int(self.num) == 5:
            self.TASK5()
            self.num += 1

        elif int(self.num) == 6:
            self.TASK6()
            self.num += 1

        elif int(self.num) == 7:
            self.TASK7()
            self.num += 1

        elif int(self.num) == 8:
            self.TASK8()
            self.num += 1

        elif int(self.num) == 9:
            self.TASK9()
            self.num += 1

        elif int(self.num) == 10:

            self.TASK10()
            self.num += 1

        elif int(self.num) == 11:

            self.TASK11()
            self.num += 1

        elif int(self.num) == 12:

            self.TASK12()
            self.num += 1

        elif int(self.num) == 13:

            self.TASK13()
            self.num += 1

        elif int(self.num) == 14:

            self.TASK14()
            self.num += 1

        elif int(self.num) == 15:

            self.TASK15()
            self.num += 1

        elif int(self.num) == 16:

            self.TASK16()
            self.num += 1

        elif int(self.num) == 17:

            self.TASK17()
            self.num += 1

        elif int(self.num) == 18:

            self.TASK18()


