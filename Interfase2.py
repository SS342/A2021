import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ModelHotel import ModelHotel
import sqlite3
from Function import Functions as Fs

class Interfase2:

    def __init__(self, name, midlle_name, surname, num):

        self.window = tk.Tk()
        self.window.geometry('1300x700')
        self.window.title('А2021: обучение расчету ADR, Occupancy, RevPar')

        self.name = name
        self.surname = surname
        self.midlle_name = midlle_name
        self.num = num

        self.conn = sqlite3.connect('testDB.db')
        self.cursor = self.conn.cursor()


        # Создание вкладок
        self.control = ttk.Notebook(self.window)

        self.tab1 = ttk.Frame(self.control)

        self.control.add(
            self.tab1,
            text='Приветствие'
                    )

        self.control.pack(
            expand=1,
            fill='both'
                     )

        self.tab2 = ttk.Frame(self.control)

        self.control.add(
            self.tab2,
            text='Виртуальная гостиница'
                    )

        self.control.pack(
            expand=1,
            fill='both'
                     )

        self.tab3 = ttk.Frame(self.control)

        self.control.add(
            self.tab3,
            text='ADR'
                    )

        self.control.pack(
            expand=1,
            fill='both'
                     )

        self.tab4 = ttk.Frame(self.control)

        self.control.add(
            self.tab4,
            text='Occupancy'
                    )

        self.control.pack(
            expand=1,
            fill='both'
                     )

        self.tab5 = ttk.Frame(self.control)

        self.control.add(
            self.tab5,
            text='RevPar'
                    )

        self.control.pack(
            expand=1,
            fill='both'
                     )

        self.tab6 = ttk.Frame(self.control)

        self.control.add(
            self.tab6,
            text='Итоговый тест'
                    )

        self.control.pack(
            expand=1,
            fill='both'
                     )

        # Создание вкладок


        # приветствие

        self.hello_txt = """
        В гостиничном бизнесе существует несколько показателей эффективности его работы.\n Одними из основных являются ADR, Occupancy, RevPar.\n В данной программе Вы научитесь вычислять эти показатели на примере виртуальной гостиницы,\n состоящей из 10 номеров Программа разделена на 6 блоков:\n     - Предисловие (текущий блок), \n   - Создание Виртуальной гостиницы,\n    - ADR,\n     - Occupancy,\n    - RevPar,\n    - Итоговый тест.\n В блоке «Виртуальная гостиница» представлена предзаполненная модель гостиницы – указаны номера,\n отчет о продаже номеров гостиницы за месяц, указав, какие из номеров были проданы и по какой цене.\n В блоках ADR. Occupancy и RevPar даются краткие теоретические сведения по показателям и методам их  расчета.\n Затем предлагается выполнить упражнения для закрепления навыка вычисления указанных  параметров В блоке «Итоговый тест»\n предлагается пройти итоговое тестирование на понимание ADR. Occupancy, RevPar и способов их вычисления.\n По итогам тестирования Вам будет выставлена оценка и выданы  соответствующие комментарии.\n  Блоки ADR. Occupancy и RevPar Вы можете осваивать в любом порядке.\n Блок «Итоговый тест» является  заключительным.\n\n Желаем успехов в обучении!\n\n\n Дробные ответы нужно записывать через знак " . "  (точка)\nПример: 3.14
        """

        self.hello_txt = tk.Label(self.tab1,
                      text=self.hello_txt,
                      font="Arial 16"
                      )

        self.hello_txt.pack()

        # приветствие

        # self.tab2

        self.VH_TEXT = tk.Label(
            self.tab2,
            text = 'Приступите к заполнению модели виртуальной гостиницы!',
            font=(
                None,
                20
                )
        )
        self.VH_TEXT.place(
            x = 230,
            y = 0
        )

        self.VH_Button = tk.Button(
            self.tab2,
            text = 'Приступить!',
            width = 15,
            command = lambda :ModelHotel(self.tab2, self.VH_TEXT,self.VH_Button)

        )
        self.VH_Button.place(
            x =400,
            y = 50
        )

        # virtual hotel wait for it

        # self.tab2


        # self.tab3
        # ADR
        # описние ADR
        self.ADR_txt1 = 'ADR, Average Daily Rate - средняя цена номера. Это усредненный показатель, демонстрирующий стоимость'
        self.ADR_txt2 = 'проданного номера за определенный период времени. ADR не включает налоги, питание и другие услуги,'
        self.ADR_txt3 = 'заложенные в стоимость проживания. Измеряется в денежных единицах. '
        self.ADR_txt4 = 'Формула расчета ADR: '

        self.ADR_txt5 = '''
Выручка от продажи номеров за период. 
        ----------------------------------------------------------------------------   = ADR
Количество проданных номеров за период.  
        '''

        self.ADR_txt6 = 'ADR, по сути, показывает стоимость услуги проживания в отеле. Этот показатель позволяет сравнивать '
        self.ADR_txt7 = 'положение дел в сети отелей, видеть свою позицию в конкурентной среде, понимать оптимальность загрузки гостиницы'


        self.ADR_TXT1 = tk.Label(
            self.tab3,
            text = self.ADR_txt1,
            font=(
                None,
                10
                )
        )

        self.ADR_TXT1.place(
            x = 0,
            y = 0
        )



        self.ADR_TXT2 = tk.Label(
            self.tab3,
            text = self.ADR_txt2,
            font=(
                None,
                10
                )
        )

        self.ADR_TXT2.place(
            x = 0,
            y = 20
              )


        self.ADR_TXT3 = tk.Label(
            self.tab3,
            text = self.ADR_txt3,
            font=(
                None,
                10
                )
        )

        self.ADR_TXT3.place(
            x = 0,
            y = 40
        )

        self.ADR_TXT4 = tk.Label(
            self.tab3,
            text = self.ADR_txt4,
            font=(
                None,
                10
                )
        )

        self.ADR_TXT4.place(
            x = 0,
            y = 60
        )


        self.ADR_TXT5 = tk.Label(
            self.tab3,
            text = self.ADR_txt5,
            font=(
                None,
                10
                )
        )

        self.ADR_TXT5.place(
            x = 0,
            y = 80
        )

        self.ADR_TXT6 = tk.Label(
            self.tab3,
            text = self.ADR_txt6,
            font=(
                None,
                10
                )
        )

        self.ADR_TXT6.place(
            x = 0,
            y = 160
        )


        self.ADR_TXT7 = tk.Label(
            self.tab3,
            text = self.ADR_txt7,
            font=(
                None,
                10
                )
        )

        self.ADR_TXT7.place(
            x = 0,
            y = 180
        )
        #описние ADR

        #Уражнения

        self.ADR_task1_1 = 'Упражнение 1.'
        self.ADR_task1_2 = 'Посчитайте ADR виртуальной гостиницы за первую неделю февраля 2021 г. Результат округлите до рублей. '

        self.ADR_task2_1 = 'Упражнение 2.'
        self.ADR_task2_2 = 'Посчитайте ADR виртуальной гостиницы за первую декаду февраля 2021 г. Результат округлите до рублей.  '

        self.ADR_task3_1 = 'Упражнение 3.'
        self.ADR_task3_2 = 'Посчитайте ADR виртуальной гостиницы за февраль 2021 г. Результат округлите до рублей.'

        self.ADR_task4_1 = 'Упражнение 4. '
        self.ADR_task4_2 = 'Предположим, известны следующие показатели отелей конкурентов виртуальному отелю за февраль 2021 года: '

        self.ADR_task4_3 = """
                            Название                          Выручка          Кол-во проданных номеров
      «Мой город»                        504 000 р                      252  
    «Уютный уголок»                   344 000 р                       164 
    «Домашнее тепло»                 500 000 р                       200\n 
          Вычислите ADR конкурентной группы за февраль 2021 года. Результат округлите до рублей.
        """

        self.ADR_task5_1 = 'Упражнение 5.'
        self.ADR_task5_2 ='Предположим, ADR конкурентной группы виртуального отеля составляет 3 678 р, а ADR виртуального отеля 3 890 р. На '
        self.ADR_task5_3 = 'сколько процентов показатель ADR виртуального отеля выше конкурентной группы? Результат округлите до сотых процента.'

        # TASK 1 in ADR
        self.ADR_TASK1_1 = tk.Label(
            self.tab3,
            text = self.ADR_task1_1,
            font=(
                None,
                10
                )
        )

        self.ADR_TASK1_1.place(
            x = 0,
            y = 220
        )

        self.ADR_TASK1_2 = tk.Label(
            self.tab3,
            text=self.ADR_task1_2,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK1_2.place(
            x=0,
            y=240
        )
        # TASK 1 in ADR

        # TASK 2 in ADR
        self.ADR_TASK2_1 = tk.Label(
            self.tab3,
            text=self.ADR_task2_1,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK2_1.place(
            x=0,
            y=280
        )

        self.ADR_TASK2_2 = tk.Label(
            self.tab3,
            text=self.ADR_task2_2,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK2_2.place(
            x=0,
            y=300
        )
        # TASK 2 in ADR

        # TASK 3 in ADR
        self.ADR_TASK3_1 = tk.Label(
            self.tab3,
            text=self.ADR_task3_1,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK3_1.place(
            x=0,
            y=340
        )

        self.ADR_TASK3_2 = tk.Label(
            self.tab3,
            text=self.ADR_task3_2,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK3_2.place(
            x=0,
            y=360
        )
        # TASK 3 in ADR

        # TASK 4 in ADR
        self.ADR_TASK4_1 = tk.Label(
            self.tab3,
            text=self.ADR_task4_1,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK4_1.place(
            x=0,
            y=400
        )

        self.ADR_TASK4_2 = tk.Label(
            self.tab3,
            text=self.ADR_task4_2,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK4_2.place(
            x=0,
            y=420
        )

        self.ADR_TASK4_3 = tk.Label(
            self.tab3,
            text=self.ADR_task4_3,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK4_3.place(
            x=0,
            y=440
        )
        # TASK 4 in ADR

        # TASK 5 in ADR
        self.ADR_TASK5_1 = tk.Label(
            self.tab3,
            text=self.ADR_task5_1,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK5_1.place(
            x=0,
            y=560
        )

        self.ADR_TASK5_2 = tk.Label(
            self.tab3,
            text=self.ADR_task5_2,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK5_2.place(
            x=0,
            y=580
        )

        self.ADR_TASK5_3 = tk.Label(
            self.tab3,
            text=self.ADR_task5_3,
            font=(
                None,
                10
            )
        )

        self.ADR_TASK5_3.place(
            x=0,
            y=600
        )
        # TASK 5 in ADR

        # Entry for answer of TASK

        self.ADRTASK1_Entry = tk.Entry(
            self.tab3,
            width = 25
        )

        self.ADRTASK1_Entry.place(
            x = 800,
            y = 250
        )

        self.ADRTASK2_Entry = tk.Entry(
            self.tab3,
            width=25
        )

        self.ADRTASK2_Entry.place(
            x=800,
            y=310
        )

        self.ADRTASK3_Entry = tk.Entry(
            self.tab3,
            width=25

        )
        self.ADRTASK3_Entry.place(
            x=800,
            y=370
        )

        self.ADRTASK4_Entry = tk.Entry(
            self.tab3,
            width=25
        )

        self.ADRTASK4_Entry.place(
            x=800,
            y=460
        )

        self.ADRTASK5_Entry = tk.Entry(
            self.tab3,
            width=25

        )
        self.ADRTASK5_Entry.place(
            x=800,
            y=430 + 160
        )

        # Entry for answer of TASK
        # create button

        self.text_Button = 'Оставить ответ'

        self.ADRTASK_Button1 = tk.Button(
            self.tab3,
            text = self.text_Button,
            command = lambda: self.ADR_TASK1()
        )

        self.ADRTASK_Button1.place(
            x = 800 + 160,
            y = 245
        )

        self.ADRTASK_Button2 = tk.Button(
            self.tab3,
            text=self.text_Button,
            command = lambda: self.ADR_TASK2()
        )

        self.ADRTASK_Button2.place(
            x=800 + 160,
            y=310 - 5
        )

        self.ADRTASK_Button3 = tk.Button(
            self.tab3,
            text=self.text_Button,
            command = lambda: self.ADR_TASK3()
        )

        self.ADRTASK_Button3.place(
            x=800 + 160,
            y=370 - 5
        )

        self.ADRTASK_Button4 = tk.Button(
            self.tab3,
            text=self.text_Button,
            command = lambda: self.ADR_TASK4()
        )

        self.ADRTASK_Button4.place(
            x=800 + 160,
            y=460 - 5
        )

        self.ADRTASK_Button5 = tk.Button(
            self.tab3,
            text=self.text_Button,
            command = lambda: self.ADR_TASK5()
        )

        self.ADRTASK_Button5.place(
            x=800 + 160,
            y=430 + 160 - 5
        )

        # ADR
        # self.tab3



        # self tab4
        # occupancy

        # text for occupancy block
        self.occ_TEXT1 = 'Occupancy'
        self.occ_TEXT2 = 'Загрузка, или Occupancy, отражает уровень заполняемости отеля. Выражается в %. '
        self.occ_TEXT3 = 'Формула расчета загрузки: '

        self.occ_TEXT4 = """
   Количество проданных номеров за период. 
                                       --------------------------------------------------------------------    =  Occupancy, загрузка
    Количество доступных номеров за период.    
        """

        self.occ_TEXT5 = 'На уровень загрузки, в частности, влияет величина отеля (чем больше отель, тем сложнее его заполнить) и ADR.  '

        self.occ_TASK1_1 = 'Упражнение 1.'
        self.occ_TASK1_2 = 'Посчитайте загрузку виртуальной гостиницы за первую неделю февраля 2021 г. Результат округлите до сотых процента. '

        self.occ_TASK2_1 = 'Упражнение 2. '
        self.occ_TASK2_2 = 'Посчитайте загрузку виртуальной гостиницы за первую декаду февраля 2021 г. Результат округлите до сотых процента.'

        self.occ_TASK3_1 = 'Упражнение 3.  '
        self.occ_TASK3_2 = 'Посчитайте загрузку виртуальной гостиницы за февраль 2021 г. Результат округлите до сотых процента.  '

        self.occ_TASK4_1 = 'Упражнение 4.'
        self.occ_TASK4_2 = 'Предположим, известны следующие показатели отелей конкурентов виртуальному отелю за февраль 2021 года:  '

        self.occ_TASK4_3 = """
        Название                              Кол-во проданных номеров        Кол-во доступных номеров
        «Мой город»                                          252                                               429
        «Уютный уголок»                                 164                                               252
        «Домашнее тепло»                              200                                               364
        Вычислите загрузку конкурентной группы за феврал 2021 года. Результат округлите до сотых процента. 
        """

        self.occ_TASK5_1 = 'Упражнение 5.'
        self.occ_TASK5_2 = 'Предположим, в гостинице с номерным фондом 265 номеров загрузка в феврале 2021 года составила 60% Какое '
        self.occ_TASK5_3 = 'количество номеров было продано отелем в этом месяце?  '
        # text for occupancy block

        # OCCUPANCY TEXT PLACE

        self.occ_TEXT1 = tk.Label(
            self.tab4,
            text = self.occ_TEXT1,
            font=(
                None,
                10
            )
        )

        self.occ_TEXT1.place(
            x = 0,
            y = 0
        )

        self.occ_TEXT2 = tk.Label(
            self.tab4,
            text=self.occ_TEXT2,
            font=(
                None,
                10
            )
        )

        self.occ_TEXT2.place(
            x=0,
            y=20
        )


        self.occ_TEXT3 = tk.Label(
            self.tab4,
            text=self.occ_TEXT3,
            font=(
                None,
                10
            )
        )

        self.occ_TEXT3.place(
            x=0,
            y=40
        )

        self.occ_TEXT4 = tk.Label(
            self.tab4,
            text=self.occ_TEXT4,
            font=(
                None,
                10
            )
        )

        self.occ_TEXT4.place(
            x=0,
            y=60
        )

        self.occ_TEXT5 = tk.Label(
            self.tab4,
            text=self.occ_TEXT5,
            font=(
                None,
                10
            )
        )

        self.occ_TEXT5.place(
            x=0,
            y=140
        )

        # OCCUPANCY TEXT PLACE

        # OCCUPANCY TASK 1

        self.occ_TASK1_1 = tk.Label(
            self.tab4,
            text = self.occ_TASK1_1,
            font=(
                None,
                10
            )
        )

        self.occ_TASK1_1.place(
            x = 0,
            y = 180
        )

        self.occ_TASK1_2 = tk.Label(
            self.tab4,
            text=self.occ_TASK1_2,
            font=(
                None,
                10
            )
        )

        self.occ_TASK1_2.place(
            x=0,
            y=200
        )

        # OCCUPANCY TASK 1


        # OCCUPANCY TASK 2

        self.occ_TASK2_1 = tk.Label(
            self.tab4,
            text=self.occ_TASK2_1,
            font=(
                None,
                10
            )
        )

        self.occ_TASK2_1.place(
            x=0,
            y=240
        )

        self.occ_TASK2_2 = tk.Label(
            self.tab4,
            text=self.occ_TASK2_2,
            font=(
                None,
                10
            )
        )

        self.occ_TASK2_2.place(
            x=0,
            y=260
        )

        # OCCUPANCY TASK 2

        # OCCUPANCY TASK 3

        self.occ_TASK3_1 = tk.Label(
            self.tab4,
            text=self.occ_TASK3_1,
            font=(
                None,
                10
            )
        )

        self.occ_TASK3_1.place(
            x=0,
            y=300
        )

        self.occ_TASK3_2 = tk.Label(
            self.tab4,
            text=self.occ_TASK3_2,
            font=(
                None,
                10
            )
        )

        self.occ_TASK3_2.place(
            x=0,
            y=320
        )

        # OCCUPANCY TASK 3

        # OCCUPANCY TASK 4

        self.occ_TASK4_1 = tk.Label(
            self.tab4,
            text=self.occ_TASK4_1,
            font=(
                None,
                10
            )
        )

        self.occ_TASK4_1.place(
            x=0,
            y=360
        )

        self.occ_TASK4_2 = tk.Label(
            self.tab4,
            text=self.occ_TASK4_2,
            font=(
                None,
                10
            )
        )

        self.occ_TASK4_2.place(
            x=0,
            y=380
        )

        self.occ_TASK4_3 = tk.Label(
            self.tab4,
            text=self.occ_TASK4_3,
            font=(
                None,
                10
            )
        )

        self.occ_TASK4_3.place(
            x=0,
            y=400
        )

        # OCCUPANCY TASK 4

        # OCCUPANCY TASK 5

        self.occ_TASK5_1 = tk.Label(
            self.tab4,
            text=self.occ_TASK5_1,
            font=(
                None,
                10
            )
        )

        self.occ_TASK5_1.place(
            x=0,
            y=520
        )

        self.occ_TASK5_2 = tk.Label(
            self.tab4,
            text=self.occ_TASK5_2,
            font=(
                None,
                10
            )
        )

        self.occ_TASK5_2.place(
            x=0,
            y=540
        )

        self.occ_TASK5_3 = tk.Label(
            self.tab4,
            text=self.occ_TASK5_3,
            font=(
                None,
                10
            )
        )

        self.occ_TASK5_3.place(
            x=0,
            y=560
        )

        # OCCUPANCY TASK 5

        # OCCUPANCY ENTRY

        self.occ_Entry1 = tk.Entry(
            self.tab4,
            width = 25
        )
        self.occ_Entry1.place(
            x = 800,
            y = 200 + 5

        )

        self.occ_Entry2 = tk.Entry(
            self.tab4,
            width=25
        )
        self.occ_Entry2.place(
            x=800,
            y=260 + 5

        )

        self.occ_Entry3 = tk.Entry(
            self.tab4,
            width=25
        )
        self.occ_Entry3.place(
            x=800,
            y=320 + 5

        )

        self.occ_Entry4 = tk.Entry(
            self.tab4,
            width=25
        )
        self.occ_Entry4.place(
            x=800,
            y=420 + 5

        )

        self.occ_Entry5 = tk.Entry(
            self.tab4,
            width=25
        )
        self.occ_Entry5.place(
            x=800,
            y=540 + 5

        )
        # OCCUPANCY ENTRY


        # OCCUPANCY BUTTONS

        self.occTASK_Button1 = tk.Button(
            self.tab4,
            text=self.text_Button,
            command = lambda: self.OCC_TASK1()
        )

        self.occTASK_Button1.place(
            x=800 + 160,
            y=200
        )

        self.occTASK_Button2 = tk.Button(
            self.tab4,
            text=self.text_Button,
            command = lambda: self.OCC_TASK2()
        )

        self.occTASK_Button2.place(
            x=800 + 160,
            y=260
        )

        self.occTASK_Button3 = tk.Button(
            self.tab4,
            text=self.text_Button,
            command = lambda: self.OCC_TASK3()
        )

        self.occTASK_Button3.place(
            x=800 + 160,
            y=320
        )

        self.occTASK_Button4 = tk.Button(
            self.tab4,
            text=self.text_Button,
            command = lambda: self.OCC_TASK4()
        )

        self.occTASK_Button4.place(
            x=800 + 160,
            y=420
        )


        self.occTASK_Button5 = tk.Button(
            self.tab4,
            text=self.text_Button,
            command = lambda: self.OCC_TASK5()
        )

        self.occTASK_Button5.place(
            x=800 + 160,
            y=540
        )

        # OCCUPANCY BUTTONS
        # self tab4
        # occupancy

        # REVPAR
        # self.tab5
        # TEXT
        self.RevPar_TEXT1  = 'RevPar (Revenu per available room per day) – выручка на доступный номер в день, по сути, отражает доходность номера. Измеряется в денежных единицах. '
        self.RevPar_TEXT2 = 'Формула расчета RevPar:'

        self.RevPar_TEXT3_1 = "     Выручка от продажи номеров за период"
        self.RevPar_TEXT3_2 = '------------------------------------------------------------------------------    =   RevPar         Либо       RevPar = ADR * Occupancy '
        self.RevPar_TEXT3_3 = '     Количество доступных номеров за период '

        self.RevPar_TEXT4 = 'RevPar позволяет понять эффективность гостиницы при сравнении с рыночными показателями и при сравнении'
        self.RevPar_TEXT5 = 'с RevPar за аналогичный период прошлых лет. '

        # TEXT

        # TEXT PLACE

        self.RevPar_TEXT1 = tk.Label(
            self.tab5,
            text = self.RevPar_TEXT1,
            font=(
                None,
                10
            )
        )

        self.RevPar_TEXT1.place(
            x = 0,
            y = 0
        )

        self.RevPar_TEXT2 = tk.Label(
            self.tab5,
            text=self.RevPar_TEXT2,
            font=(
                None,
                10
            )
        )

        self.RevPar_TEXT2.place(
            x=0,
            y=20
        )

        self.RevPar_TEXT3_1 = tk.Label(
            self.tab5,
            text=self.RevPar_TEXT3_1,
            font=(
                None,
                10
            )
        )

        self.RevPar_TEXT3_1.place(
            x=0,
            y=60
        )
        self.RevPar_TEXT3_2 = tk.Label(
            self.tab5,
            text=self.RevPar_TEXT3_2,
            font=(
                None,
                10
            )
        )

        self.RevPar_TEXT3_2.place(
            x=0,
            y=80
        )
        self.RevPar_TEXT3_3 = tk.Label(
            self.tab5,
            text=self.RevPar_TEXT3_3,
            font=(
                None,
                10
            )
        )

        self.RevPar_TEXT3_3.place(
            x=0,
            y=100
        )

        self.RevPar_TEXT4 = tk.Label(
            self.tab5,
            text=self.RevPar_TEXT4,
            font=(
                None,
                10
            )
        )

        self.RevPar_TEXT4.place(
            x=0,
            y=120
        )

        self.RevPar_TEXT5 = tk.Label(
            self.tab5,
            text=self.RevPar_TEXT5,
            font=(
                None,
                10
            )
        )

        self.RevPar_TEXT5.place(
            x=0,
            y=140
        )


        # RevPar TASK

        self.RevPar_TASK1_1 = 'Упражнение 1. '
        self.RevPar_TASK1_2 = 'Посчитайте RevPar виртуальной гостиницы за первую неделю февраля 2021 г. Результат округлите до рублей. '

        self.RevPar_TASK2_1 = 'Упражнение 2.'
        self.RevPar_TASK2_2 = 'Посчитайте RevPar виртуальной гостиницы за первую декаду февраля 2021 г. Результат округлите до рублей. '

        self.RevPar_TASK3_1 = 'Упражнение 3.'
        self.RevPar_TASK3_2 = 'Посчитайте RevPar виртуальной гостиницы за февраль 2021 г. Результат округлите до рублей.'

        self.RevPar_TASK4_1 = 'Упражнение 4.'
        self.RevPar_TASK4_2 = 'Предположим, известны следующие показатели отелей конкурентов виртуальному отелю за февраль 2021 года:'

        self.RevPar_TASK4_3 ="""
        Название                      Выручка от продажи номеров    Кол-во доступных номеров
«Мой город»                                   504 000 р                                              429
«Уютный уголок»                           344 400 р                                              252
«Домашнее тепло»                        500 000 р                                             364
Вычислите RevPar конкурентной группы за февраль 2021 года. Результат округлите до рублей.  
        """

        self.RevPar_TASK5_1 = 'Упражнение 5. '
        self.RevPar_TASK5_2 = 'Предположим, RevPar конкурентной группы виртуального отеля за январь 2021 г составляет 1 350 р, а количество '
        self.RevPar_TASK5_3 = 'доступных номеров в этом месяце было 950 единиц. Определите выручку от продажи номерного фонда конкурентной группы?  '

        self.RP_TASK1_1 = tk.Label(
            self.tab5,
            text = self.RevPar_TASK1_1,
            font=(
                None,
                10
            )
        )

        self.RP_TASK1_1.place(
            x = 0,
            y = 180
        )

        self.RP_TASK1_2 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK1_2,
            font=(
                None,
                10
            )
        )

        self.RP_TASK1_2.place(
            x=0,
            y=200
        )

        self.RP_TASK2_1 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK2_1,
            font=(
                None,
                10
            )
        )

        self.RP_TASK2_1.place(
            x=0,
            y=240
        )

        self.RP_TASK2_2 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK2_2,
            font=(
                None,
                10
            )
        )

        self.RP_TASK2_2.place(
            x=0,
            y=260
        )

        self.RP_TASK3_1 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK3_1,
            font=(
                None,
                10
            )
        )

        self.RP_TASK3_1.place(
            x=0,
            y=300
        )

        self.RP_TASK3_2 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK3_2,
            font=(
                None,
                10
            )
        )

        self.RP_TASK3_2.place(
            x=0,
            y=320
        )

        self.RP_TASK4_1 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK4_1,
            font=(
                None,
                10
            )
        )

        self.RP_TASK4_1.place(
            x=0,
            y=360
        )

        self.RP_TASK4_2 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK4_2,
            font=(
                None,
                10
            )
        )

        self.RP_TASK4_2.place(
            x=0,
            y=380
        )

        self.RP_TASK4_3 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK4_3,
            font=(
                None,
                10
            )
        )

        self.RP_TASK4_3.place(
            x=0,
            y=400
        )

        self.RP_TASK5_1 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK5_1,
            font=(
                None,
                10
            )
        )

        self.RP_TASK5_1.place(
            x=0,
            y=520
        )

        self.RP_TASK5_2 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK5_2,
            font=(
                None,
                10
            )
        )

        self.RP_TASK5_2.place(
            x=0,
            y=540
        )

        self.RP_TASK5_3 = tk.Label(
            self.tab5,
            text=self.RevPar_TASK5_3,
            font=(
                None,
                10
            )
        )

        self.RP_TASK5_3.place(
            x=0,
            y=560
        )


        # RevPar ENTRY

        self.RP_Entry1 = tk.Entry(
            self.tab5,
            width = 25
        )

        self.RP_Entry1.place(
            x = 800,
            y = 200
        )

        self.RP_Entry2 = tk.Entry(
            self.tab5,
            width=25
        )

        self.RP_Entry2.place(
            x=800,
            y=260
        )

        self.RP_Entry3 = tk.Entry(
            self.tab5,
            width=25
        )

        self.RP_Entry3.place(
            x=800,
            y=320
        )

        self.RP_Entry4 = tk.Entry(
            self.tab5,
            width=25
        )

        self.RP_Entry4.place(
            x=800,
            y=420
        )

        self.RP_Entry5 = tk.Entry(
            self.tab5,
            width=25
        )

        self.RP_Entry5.place(
            x=800,
            y=540
        )


        #RevPar BUTTONS

        self.RP_Button1 = tk.Button(
            self.tab5,
            text=self.text_Button,
            command = lambda: self.RP_TASK1()
        )

        self.RP_Button1.place(
            x=800 + 160,
            y=200 - 5
        )

        self.RP_Button2 = tk.Button(
            self.tab5,
            text=self.text_Button,
            command = lambda: self.RP_TASK2()
        )

        self.RP_Button2.place(
            x=800 + 160,
            y=260 - 5
        )

        self.RP_Button3 = tk.Button(
            self.tab5,
            text=self.text_Button,
            command = lambda: self.RP_TASK3()
        )

        self.RP_Button3.place(
            x=800 + 160,
            y=320 - 5
        )

        self.RP_Button4 = tk.Button(
            self.tab5,
            text=self.text_Button,
            command = lambda: self.RP_TASK5()
        )

        self.RP_Button4.place(
            x=800 + 160,
            y=540 - 5
        )

        self.RP_Button5 = tk.Button(
            self.tab5,
            text='self.text_Button',
            command = lambda: self.RP_TASK4()
        )

        self.RP_Button5.place(
            x=800 + 160,
            y=420 - 5
        )


        # REVPAR ALL

        #General Tab
        # self.tab6

        self.zadanie = 1  #
        self.adr = 0
        self.occ = 0
        self.revpar = 0

        self.group_1 = tk.IntVar()


        self.num_zadanie1 = 'Задание 1 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie2 = 'Задание 2 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie3 = 'Задание 3 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie4 = 'Задание 4 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie5 = 'Задание 5 из 18\n\n\n\n\n\n\n\n\n\n'

        self.num_zadanie6 = 'Задание 6 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie7 = 'Задание 7 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie8 = 'Задание 8 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie9 = 'Задание 9 из 18\n\n\n\n\n\n\n\n\n\n'

        self.num_zadanie10 = 'Задание 10 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie11 = 'Задание 11 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie12 = 'Задание 12 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie13 = 'Задание 13 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie14 = 'Задание 14 из 18\n\n\n\n\n\n\n\n\n\n'

        self.num_zadanie15 = 'Задание 15 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie16 = 'Задание 16 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie17 = 'Задание 17 из 18\n\n\n\n\n\n\n\n\n\n'
        self.num_zadanie18 = 'Задание 18 из 18\n\n\n\n\n\n\n\n\n\n'

        self.GENERAL_TASK1 = '1. Доходность номера показывает … : '
        self.GENERAL_TASK2 = '2. Отношение количества проданных номеров за период\n к количеству доступных номеров за этот же период – это …: '
        self.GENERAL_TASK3 = '3. Средняя стоимость номера за период,\n умноженная на количество проданных номеров за период – это …: '
        self.GENERAL_TASK4 = '4. Выручка от продажи номеров за период / Количество проданных номеров за период показывает:'
        self.GENERAL_TASK5 = '5. Количество проданных номеров за период / количество доступных номеров за период показывает: '
        self.GENERAL_TASK6 = "6. Выручка от продажи номеров за период / Количество доступных номеров за период показывает: "

        self.GENERAL_TASK7 = '7. Рассчитайте ADR виртуальной гостиницы за 2 декаду февраля 2021 г.\n\n '
        self.GENERAL_TASK8 = '8. Рассчитайте загрузку виртуальной гостиницы за 2 декаду февраля 2021 г.\n\n '
        self.GENERAL_TASK9 = '9. Рассчитайте RevPar виртуальной гостиницы за 2 декаду февраля 2021 г.\n\n '
        self.GENERAL_TASK10 = '10. В течение марта в гостинице к продаже было доступно 40 номеров.\n RevPar гостиницы в этот период составил 3 250 руб.\n Какая выручка была у данной гостиницы в марте? \n\n'
        self.GENERAL_TASK11 = '11. В апреле выручка гостиницы составила 3 660 000 руб, а RevPar достиг 2 928 руб.\n Определите, сколько номеров в гостинице,\n если в течение апреля в продаже был весь номерной фонд.\n\n'

        self.GENERAL_TASK12 = '12. Чему равна средняя цена номера,\n если при загрузке 55% выручка на доступный номер в день составляет 2 475 руб? \n\n'
        self.GENERAL_TASK13 = '13. Средняя цена номера в мае составила 4 700 руб,\n при этом выручка на доступный номер в день была 2 900 руб.\n Определите загрузку номерного фонда в мае. Результат запишите с точностью до десятых.\n\n  '
        self.GENERAL_TASK14 = '14. В июне в отеле продали 600 номеров.\n Загрузка отеля в этот месяц составила 50%. Сколько номеров было в продаже в июне? \n\n'
        self.GENERAL_TASK15 = '15. В сентябре номерной фонд гостиницы составлял 30 номеров.\n Ни один номер в течение этого периода не выводился из продажи.\n Определите количество номеров, проданных за этот период, если загрузка составила 63,3%.\n\n '
        self.GENERAL_TASK16 = '16. Средняя цена номера в мае составила 4 500 руб.\n За этот месяц было продано 1 650 номеров.\n Какова выручка гостиницы от продажи номеров за этот период? \n\n'
        self.GENERAL_TASK17 = '17. Выручка гостиницы в августе составила 4 882 500 руб.,\n а средняя цена за номер в этот период была 4 500 руб. Сколько номеров в гостинице,\n если в августе в продаже был весь номерной фонд.\n\n '
        self.GENERAL_TASK18 = '18. Чему равна доходность номера, если в течение августа в продаже было 17 номеров,\n а выручка от реализации номеров составила 1 475 600 руб.\n\n'


        self.rad1 = tk.Radiobutton(
            self.tab6,
            text='ARD',
            value=1,
            variable=self.group_1
                                   )

        self.rad2 = tk.Radiobutton(
            self.tab6,
            text='PaRev',
            value=2,
            variable=self.group_1
        )

        self.rad3 = tk.Radiobutton(
            self.tab6,
            text='RevPar',
            value=3,
            variable=self.group_1
        )

        self.rad4 = tk.Radiobutton(
            self.tab6,
            text='Occupancy',
            value=4,
            variable=self.group_1
        )

        self.rad5 = tk.Radiobutton(
            self.tab6,
            text='ADR',
            value=5,
            variable=self.group_1
        )

        #############


        self.FS = Fs(self.name, self.midlle_name, self.surname, self.num)



        #############

        self.GTASK1txt = tk.Label(
            self.tab6,
            text = self.num_zadanie1,
            font=(
                None,
                10
            )
        )

        self.TASK1 = tk.Label(
            self.tab6,
            text = self.GENERAL_TASK1,
            font=(
                None,
                20
            )

        )


        self.GENERALTASK_LIST = [
            self.GENERAL_TASK1, self.GENERAL_TASK2,  self.GENERAL_TASK3, self.GENERAL_TASK4,
            self.GENERAL_TASK5, self.GENERAL_TASK6, self.GENERAL_TASK7, self.GENERAL_TASK8, self.GENERAL_TASK9,
            self.GENERAL_TASK10, self.GENERAL_TASK11, self.GENERAL_TASK12, self.GENERAL_TASK13, self.GENERAL_TASK14,
            self.GENERAL_TASK15, self.GENERAL_TASK16, self.GENERAL_TASK17, self.GENERAL_TASK18
        ]


        self.num_zadanie = [
            self.num_zadanie1, self.num_zadanie2, self.num_zadanie3, self.num_zadanie4, self.num_zadanie5,
            self.num_zadanie6, self.num_zadanie7, self.num_zadanie8, self.num_zadanie9, self.num_zadanie10,
            self.num_zadanie11, self.num_zadanie12, self.num_zadanie13, self.num_zadanie14, self.num_zadanie15,
            self.num_zadanie16, self.num_zadanie17, self.num_zadanie18
        ]


        self.GTASK1txt.pack(side = tk.TOP)
        self.TASK1.pack(side = tk.TOP)

        self.rad1.pack()
        self.rad2.pack()
        self.rad3.pack()
        self.rad4.pack()
        self.rad5.pack()

        self.RAD1 = [self.rad1, self.rad2, self.rad3, self.rad4, self.rad5]

        self.GENERALBUTTON1 = tk.Button(
            self.tab6,
            text="Дальше ->",
            width=20,
            background="#DCDCDC",
            command=lambda: self.FS.TASK(
                self.TASK1, self.tab6, self.GENERALTASK_LIST, self.num_zadanie, self.GTASK1txt, self.RAD1, self.group_1.get(),self.GENERALBUTTON1
            )
        )

        self.GENERALBUTTON1.pack(side=tk.BOTTOM)



    def ADR_TASK1(self):

        sql = "SELECT number from settings Where id = '1'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.SEVENDAY_ADR = tmp[0][0]
        print(str(round(self.SEVENDAY_ADR)))
        if float(self.ADRTASK1_Entry.get()) == float(round(self.SEVENDAY_ADR)):

            messagebox.showinfo(None,"Правильно!")

        else:

            messagebox.showinfo(None,"Неправильно")

        self.ADRTASK1_Entry.delete(
            0,
            last=tk.END
        )


    def ADR_TASK2(self):

        sql = "SELECT number from settings Where id = '2'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.DECADA_ADR = tmp[0][0]
        print(str(round(self.DECADA_ADR)))
        if self.ADRTASK2_Entry.get() == str(round(self.DECADA_ADR)):

            messagebox.showinfo(None,"Правильно!")

        else:

            messagebox.showinfo(None,"Неправильно")

        self.ADRTASK2_Entry.delete(
            0,
            last=tk.END
        )

    def ADR_TASK3(self):

        sql = "SELECT number from settings Where id = '4'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.ALL_ADR = tmp[0][0]
        print(str(round(self.ALL_ADR)))
        if self.ADRTASK3_Entry.get() == str(round(self.ALL_ADR)):

           messagebox.showinfo(None,"Правильно!")

        else:

            messagebox.showinfo(None,"Неправильно")

        self.ADRTASK3_Entry.delete(
            0,
            last=tk.END
        )

    def ADR_TASK4(self):

        if self.ADRTASK4_Entry.get() == str(2189):
            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.ADRTASK4_Entry.delete(
            0,
            last=tk.END
        )

    def ADR_TASK5(self):

        if self.ADRTASK5_Entry.get() == str(5.76) or self.ADRTASK5_Entry.get() == str('5,76'):

            messagebox.showinfo(None,"Правильно!")

        else:

            messagebox.showinfo(None,"Неправильно")

        self.ADRTASK5_Entry.delete(
            0,
            last=tk.END
        )






    def OCC_TASK1(self):

        sql = "SELECT number from settings Where id = '5'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.OCC_SEVEN_DAY = tmp[0][0]
        print(float(round(self.OCC_SEVEN_DAY,2)))
        if float(self.occ_Entry1.get()) == float((round(self.OCC_SEVEN_DAY,2))):

            messagebox.showinfo(None,"Правильно!")

        else:

            messagebox.showinfo(None,"Неправильно")

        self.occ_Entry1.delete(
            0,
            last=tk.END
        )

    def OCC_TASK2(self):

        sql = "SELECT number from settings Where id = '6'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.OCC_DECADA = tmp[0][0]
        print(str(round(self.OCC_DECADA,2)))
        if float(self.occ_Entry2.get()) == float((round(self.OCC_DECADA,2))):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.occ_Entry2.delete(
            0,
            last=tk.END
        )

    def OCC_TASK3(self):

        sql = "SELECT number from settings Where id = '8'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.OCC_ALL = tmp[0][0]
        print(str(round(self.OCC_ALL,2)))
        if float(self.occ_Entry3.get())== float((round(self.OCC_ALL,2))):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.occ_Entry3.delete(
            0,
            last=tk.END
        )

    def OCC_TASK4(self):

        if float(self.occ_Entry4.get()) == float(58.95) or self.occ_Entry4.get() == str('58,95'):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.occ_Entry4.delete(
            0,
            last=tk.END
        )

    def OCC_TASK5(self):

        if self.occ_Entry5.get() == str(159):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.occ_Entry5.delete(
            0,
            last=tk.END
        )




    def RP_TASK1(self):

        sql = "SELECT number from settings Where id = '9'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.RP_SEVEN_DAY = tmp[0][0]
        print(str(round(self.RP_SEVEN_DAY, 2)))
        if float(self.RP_Entry1.get()) == float((round(self.RP_SEVEN_DAY, 2))):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.RP_Entry1.delete(
            0,
            last=tk.END
        )

    def RP_TASK2(self):

        sql = "SELECT number from settings Where id = '10'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.RP_DECADA = tmp[0][0]
        print(str(round(self.RP_DECADA, 2)))
        if float(self.RP_Entry2.get()) == float((round(self.RP_DECADA, 2))):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.RP_Entry2.delete(
            0,
            last=tk.END
        )

    def RP_TASK3(self):

        sql = "SELECT number from settings Where id = '12'"
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        self.RP_Entry2 = tmp[0][0]
        print(str(round(self.RP_Entry2, 2)))
        if float(self.RP_Entry3.get())== float((round(self.RP_Entry2, 2))):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.RP_Entry3.delete(
            0,
            last=tk.END
        )


    def RP_TASK4(self):

        if self.RP_Entry4.get() == str(1290):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.RP_Entry4.delete(
            0,
            last=tk.END
        )


    def RP_TASK5(self):

        if self.RP_Entry5.get() == str(1282500):

            messagebox.showinfo(None, "Правильно!")

        else:

            messagebox.showinfo(None, "Неправильно")

        self.RP_Entry5.delete(
            0,
            last=tk.END
        )
