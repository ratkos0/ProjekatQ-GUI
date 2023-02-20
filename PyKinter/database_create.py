import sqlite3


def base():
    connection = sqlite3.connect('projekat.db')
    cursor = connection.cursor()
    # Kreira tabelu sa podatcima o vlasniku
    sql_command = """CREATE TABLE vozac(\
           id INTEGER PRIMARY KEY,\
           Ime VARCHAR(20),\
           Prezime VARCHAR(20),\
           Godine VARCHAR(2));"""
    cursor.execute(sql_command)

    # Kreira tabelu sa podatcima o automobilu
    sql_command2 = """CREATE TABLE auto(\
          id INTEGER PRIMARY KEY,\
          Naziv VARCHAR(20),\
          Model VARCHAR(30),\
          Tip VARCHAR(20),\
          Broj_vrata CHAR(1),\
          Motor VARCHAR(5),\
          Konjskih_snaga VARCHAR(4));"""
    cursor.execute(sql_command2)

    # Kreira tabelu sa podatcima o dodatnoj opremi koju automobil posjeduje
    sql_command1 = """CREATE TABLE dodatna_oprema(\
            id INTEGER PRIMARY KEY,\
            Parking_Senzori VARCHAR(2),\
            Alu_Felge VARCHAR(2),\
            Klima VARCHAR(2),\
            Rikverc_Kamera VARCHAR(2),\
            Grijanje_sjedista VARCHAR(2),\
            Panorama VARCHAR(2));"""
    cursor.execute(sql_command1)
    sql_command3 = """CREATE TABLE info(\
            id INTEGER PRIMARY KEY,\
            Boja VARCHAR(15),\
            Ostecenje VARCHAR(2),\
            Korozija VARCHAR(2));"""
    cursor.execute(sql_command3)
    connection.close()
