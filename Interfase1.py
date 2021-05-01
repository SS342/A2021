# Импорт библиотек !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! НЕ ТРОГАТЬ НЕ ТРОГАТЬ
import tkinter as tk  # импорт в проект библиотеки tkinter
from tkinter import messagebox  # Импорт всплывающих окон
from Interfase2 import Interfase2
# Импорт библиотек !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  НЕ ТРОГАТЬ НЕ ТРОГАТЬ

class Interfase:

    def __init__(self, conn, cursor):

        self.conn = conn
        self.cursor = cursor

        self.window = tk.Tk()

        self.window.geometry('550x300')

        self.window.title('А2021: обучение расчету ADR, Occupancy, RevPar')

        self.entry_registr = tk.Entry(self.window, width=42)
        self.entry_registr.place(x=138, y=50)

        self.entry1_registr = tk.Entry(self.window, width=42)
        self.entry1_registr.place(x=138, y=100)

        self.txt_registr = tk.Label(self.window, text='Имя:')
        self.txt_registr.place(x=205, y=28)

        self.txt1_registr = tk.Label(self.window, text='Фамилия:')
        self.txt1_registr.place(x=205, y=78)

        self.btn_registr = tk.Button(self.window, text='Вход',width = 10, command = lambda: self.Cheak(self.entry_registr.get(),self.entry1_registr.get()))
        self.btn_registr.place(x=350, y=150)

        self.window.mainloop()

    def Cheak(self,name,surame):

        name = name.lower()
        surame = surame.lower()

        sql = "SELECT * FROM user WHERE name ='" + str(name) + "' and surname = '" + str(surame) + "'"

        self.cursor.execute(sql)

        tmp = self.cursor.fetchall()

        if tmp:

            self.window.destroy()
            self.tmp = tmp[0]
            print(self.tmp)
            For_now_user_name = self.tmp[1]
            For_now_user_middle_name = self.tmp[2]
            For_now_user_surname = self.tmp[3]
            For_now_user_number = self.tmp[4]
            print('name', For_now_user_name,"mid",For_now_user_middle_name,'sur',For_now_user_surname,"num",For_now_user_number)
            Interfase2(For_now_user_name,For_now_user_middle_name, For_now_user_surname, For_now_user_number)

        else:

            return messagebox.showwarning('Предупреждение', 'Введеные данные не правильные')  # Окно предупреждения




