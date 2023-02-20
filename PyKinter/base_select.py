import sqlite3
import time

def base_select():
    #Uzima sve podatke iz baze i ispisuje ih
    connection = sqlite3.connect('projekat.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vozac, auto, dodatna_oprema, info")
    ans = cursor.fetchall()
    for i in ans:
        print(i)
        #Pet sekundi pauze do ucitavanja menija
        time.sleep(5)
