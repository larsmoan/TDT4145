import sqlite3
import os

import datetime

def create_db(filename):
    #Just a dummy name for the database
    db_filename = filename[:-4] + '.db'
    ##Remove any existing database -  makes it easier to run the script multiple times
    try:
        os.remove(db_filename)
    except OSError:
        pass
    conn = sqlite3.connect(db_filename)

    with open(filename, 'r') as sql_file:
        conn.executescript(sql_file.read())

    conn.close()


def init_db(db_filename):
    #Skal legge inn nødvendig data som ikke trenger å programmeres direkte
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    stasjons_query = """INSERT INTO Stasjon (navn, meterOverHavet) VALUES ('Trondheim', 5.1),
    ('Steinkjer',3.6), ('Mosjøen',6.8), ('Mo i Rana', 3.5), ('Fauske', 34), ('Bodø', 4.1)"""

    tog_query = """INSERT INTO Tog (TogID) VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10)"""
    rute_query = """INSERT INTO Rute (RuteID, TogID, Retning, startStasjon, endeStasjon, driftesAv) VALUES 
    (1, 1, 'MED', 'Trondheim', 'Bodø', 'SJ'),
    (2,2,'MED', 'Trondheim', 'Bodø', 'SJ'),
    (3,3, 'MOT', 'Mo i Rana', 'Trondheim', 'SJ')
    """
    operatorer_query = """INSERT INTO Operator (OperatorNavn) VALUES ('SJ'), ('Bane NOR')"""

    vogn_query = """INSERT INTO Vogn (OperatorNavn, VognID, Navn) VALUES ('SJ', 1, 'SJ-sittevogn-1'),
    ('SJ', 2, 'SJ-sittevogn-1'),
    ('SJ', 3, 'SJ-sittevogn-1'),
    ('SJ', 4, 'SJ-sittevogn-1'),
    ('SJ', 5, 'SJ-sovevogn-1')"""
    sittevogn_query = """INSERT INTO Sittevogn (OperatorNavn, VognID, antallRader, seterPerRad)
    VALUES ('SJ', 1, 3, 4),
            ('SJ', 2, 3, 4),
            ('SJ', 3, 3, 4),
            ('SJ', 4, 3, 4)"""
    sovevogn_query = """INSERT INTO SoveVogn (OperatorNavn, VognID, antallKupeer)
    VALUES ('SJ', 5, 4)"""

    rutedag_query = """INSERT INTO Rutedag(RuteID, ukedag) VALUES
    (1, 'mandag'), (1, 'tirsdag'), (1, 'onsdag'), (1, 'torsdag'), (1, 'fredag'),
    (2, 'mandag'), (2, 'tirsdag'), (2, 'onsdag'), (2, 'torsdag'), (2, 'fredag'),(2, 'lørdag'), (2, 'søndag'),
    (3, 'mandag'), (3, 'tirsdag'), (3, 'onsdag'), (3, 'torsdag'), (3, 'fredag')"""

    delavtog_query = """INSERT INTO DelAvTog (TogID, OperatorNavn, VognID, NummerIRekke) VALUES
    (1, 'SJ', 1, 1),
    (1, 'SJ', 2, 2),

    (2, 'SJ', 3, 1),
    (2, 'SJ', 5, 2),

    (3, 'SJ', 3, 1)
    """

    rutetabell_query = """INSERT INTO RuteTabell (RuteID, tabellID, StasjonsNavn, tid) VALUES
    (1, 1, 'Trondheim', '07:49'),
    (1, 2, 'Steinkjer', '09:51'),
    (1, 3, 'Mosjøen', '13:20'),
    (1, 4, 'Mo i Rana', '14:31'),
    (1, 5, 'Fauske', '16:49'),
    (1, 6, 'Bodø', '17:34'),
    
    (2, 7, 'Trondheim', '23:05'),
    (2, 8, 'Steinkjer', '00:57'),
    (2, 9, 'Mosjøen', '04:41'),
    (2, 10, 'Mo i Rana', '05:55'),
    (2, 11, 'Fauske', '08:19'),
    (2, 12, 'Bodø', '09:05'),
    
    (3, 13, 'Mo i Rana', '08:11'),
    (3, 14, 'Mosjøen', '09:14'),
    (3, 15, 'Steinkjer', '12:31'),
    (3, 16, 'Trondheim', '14:13')"""

    strekning_query = """INSERT INTO Strekning (Navn, fremdriftsEnergi) VALUES
                        ('Nordlandsbanen', 'Diesel')"""
    delstrekning_query = """INSERT INTO DelStrekning (StrekningsID, InngaarIstrekning, startStasjon, endeStasjon, lengde, antallSpor) VALUES
                            (1, 'Nordlandsbanen', 'Trondheim', 'Steinkjer', 120, 2),
                            (2, 'Nordlandsbanen', 'Steinkjer', 'Mosjøen', 280, 1),
                            (3, 'Nordlandsbanen', 'Mosjøen', 'Mo i Rana', 90, 1),
                            (4, 'Nordlandsbanen', 'Mo i Rana', 'Fauske', 170, 1),
                            (5, 'Nordlandsbanen', 'Fauske', 'Bodø', 60, 1)"""
    
    ruteforekomst_query = """INSERT INTO RuteForekomst (ForekomstID, RuteID, dato) VALUES 
                            (1, 1, '2023-03-4'),
                            (2, 2, '2023-03-4'),
                            (3, 3, '2023-03-4')
                            """
    
    c.execute(stasjons_query)
    c.execute(tog_query)
    c.execute(rute_query)
    c.execute(operatorer_query)
    c.execute(vogn_query)
    c.execute(sittevogn_query)
    c.execute(sovevogn_query)
    c.execute(rutedag_query)

    c.execute(delavtog_query)
    c.execute(rutetabell_query)
    c.execute(strekning_query)
    c.execute(delstrekning_query)
    c.execute(ruteforekomst_query)
    conn.commit()
    conn.close()

# Task c)
def get_togrute_info():
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()
    stasjon = input ("Hvilken stasjon vil du sjekke? ")
    
    #Check if the stasjon exists by reading from the table Stasjon
    c.execute("SELECT * FROM Stasjon WHERE navn = ?", (stasjon,))
    if c.fetchone() is None:
        print("Stasjonen finnes ikke")
        return
    
    #Get the ukedag from user
    ukedag = input("Hvilken ukedag? ")
    #Check if the ukedag exists by reading from the table Rutedag
    c.execute("SELECT * FROM Rutedag WHERE ukedag = ?", (ukedag,))
    if c.fetchone() is None:
        print("Ukedagen finnes ikke")
        return
    
    c.execute("""SELECT RuteID FROM (RuteTabell INNER JOIN Rutedag USING (RuteID) ) WHERE RuteDag.ukedag = ? and RuteTabell.StasjonsNavn = ? """, (ukedag, stasjon))
    
    
    ruter = c.fetchall()

    print("Følgende ruter går fra", stasjon, "på", ukedag + "er:")

    for rute in ruter:
        c.execute("SELECT * FROM Rute WHERE RuteID = ?", (rute[0],))
        ruteinfo = c.fetchall()
        print("Rute: ", ruteinfo[0][1], ruteinfo[0][2], ruteinfo[0][3], ruteinfo[0][4], ruteinfo[0][5])


    conn.close()


# Task d)
def search_routes():
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    date = input("Hvilken dato vil du sjekke  (YYYY-DD-MM) format? ")
    year, day, month = map(int, date.split('-'))
    

    stasjon1 = input("Fra hvilken stasjon vil du reise? ")
    stasjon2 = input("Til hvilken stasjon vil du reise? ")

    stasjoner = [stasjon1, stasjon2]
    
    #Check if the stasjon exists by reading from the table Stasjon
    c.execute("SELECT Stasjon.Navn FROM Stasjon")
    stasjonsnavn = c.fetchall()

    for stasjon in stasjoner:
        if (stasjon,) not in stasjonsnavn:
            print("Stasjonen finnes ikke")
            return
    
    #Find all routes from stasjon1 to stasjon2 on the given date

    #first find all ruteforekomster
    conn.execute("SELECT * FROM RuteForekomst WHERE dato = ?", (date,))
    ruteforekomster = c.fetchall()

    conn.close()
    
    print(ruteforekomster)
        


    
search_routes()

""" #These functions will create and add data about the Nordlandsbanen to the database
create_db("sql_prosjektet.sql")
init_db('sql_prosjektet.db') """




