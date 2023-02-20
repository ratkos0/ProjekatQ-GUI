import sqlite3

def database_insert():
    connection = sqlite3.connect('projekat.db')
    cursor = connection.cursor()
    username = input("Unesite Vase ime")
    surname = input("Unesite Vase prezime")
    age = int(input("Koliko imate godina"))
    # ID korisnika i vozila je isti
    identif = int(input('Unesite ID'))
    try:
        connection = sqlite3.connect('projekat.db')
        cursor = connection.cursor()
        for iden in identif:
            cursor.execute("""SELECT id FROM vozac WHERE id = ?""", (iden,))
            db_result = cursor.fetchall()
            if len(db_result) == 0:
                print("Jedinstven ID")
            else:
                print("ID se koristi")
                identif = int(input("Unesite ID"))
    except:
        pass
    name = str(input('Unesite naziv auta'))
    model = str(input('Unesite model vozila'))
    type = str(input('Unesite tip automobila'))
    car_door = int(input('Unesite broj vrata na automobilu'))
    engine = input('Unesite motor automobila')
    hp = int(input('Unesite broj konjskih snaga automobila'))
    # Podatci za dodatnu opremu automobila
    park_sens = input("Da li automobil ima parking senzore?")
    alu_felge = input("Da li automobil ima aluminijske feluge?")
    air_con = input("Da li automobil ima klimu?")
    rev_camera = input("Da li automobil ima Rikverc kameru?")
    heat_seat = input("Da li automobil ima grijanje u sjedistima?")
    panor = input("Da li automobil ima panoramu?")
    # Podatci tabele info
    # ID ostaje isti
    carcolor = input("Koje je boje automobil?")
    carcrash = input("Da li je auto nekada bilo havarisano?")
    carcorosion = input("Da li auto ima korozije negdje?")
    infolist = [(identif, carcolor, carcrash, carcorosion)]
    addons_list = [(identif, park_sens, alu_felge,
                    air_con, rev_camera, heat_seat, panor)]

    list = [(identif, name, model, type, car_door, engine, hp)]
    connection.executemany("""INSERT INTO auto(id, Naziv, Model,Tip, Broj_vrata, Motor, Konjskih_snaga) VALUES (?,?,?,?,?,?,?)""",
                           list)
    vozac_list = [(identif, username, surname, age)]
    connection.executemany(
        """INSERT INTO vozac(id, Ime, Prezime, Godine) VALUES (?,?,?,?)""", vozac_list)
    connection.executemany(
        """INSERT INTO dodatna_oprema(id, Parking_Senzori, Alu_Felge, Klima, Rikverc_Kamera, Grijanje_sjedista, Panorama) VALUES (?,?,?,?,?,?,?)""", addons_list)
    connection.executemany("""INSERT INTO info(id, Boja, Ostecenje, Korozija) VALUES (?,?,?,?)""", infolist)
    connection.commit()
    connection.close()
 
