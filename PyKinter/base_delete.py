import sqlite3
import time

def base_delete():
    #Funkcija koja brise podatke iz baze
    base_delete_input =input('Unesite ID automobila za brisanje')
    list = [(base_delete_input)]
    connection = sqlite3.connect('projekat.db')
    cursor = connection.cursor()
    connection.executemany("DELETE FROM auto WHERE id = ?", base_delete_input)
    connection.executemany("DELETE FROM dodatna_oprema WHERE id = ?", base_delete_input)
    connection.executemany("DELETE FROM vozac WHERE id = ?", base_delete_input)
    connection.commit()
    connection.close()
