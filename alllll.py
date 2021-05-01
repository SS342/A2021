from Interfase1 import Interfase
from DataBase import DataBase
import sqlite3



conn = sqlite3.connect('testDB.db')
cursor1 = conn.cursor()

DB = DataBase()
I = Interfase(conn, cursor1)
