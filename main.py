import sqlite3
import os

import datetime

def CREATE_db(filename):
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
    rute_query = """INSERT INTO Rute (RuteID, TogID, Retning, startStasjon, endeStasjon, OperatorNavn) VALUES 
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

    strekning_query = """INSERT INTO Strekning (StrekningsNavn, fremdriftsEnergi) VALUES
                        ('Nordlandsbanen', 'Diesel')"""
    delstrekning_query = """INSERT INTO DelStrekning (DelstrekningsID, StrekningsNavn, startStasjon, endeStasjon, lengde, antallSpor) VALUES
                            (1, 'Nordlandsbanen', 'Trondheim', 'Steinkjer', 120, 2),
                            (2, 'Nordlandsbanen', 'Steinkjer', 'Mosjøen', 280, 1),
                            (3, 'Nordlandsbanen', 'Mosjøen', 'Mo i Rana', 90, 1),
                            (4, 'Nordlandsbanen', 'Mo i Rana', 'Fauske', 170, 1),
                            (5, 'Nordlandsbanen', 'Fauske', 'Bodø', 60, 1)"""
    
    ruteforekomst_query = """INSERT INTO RuteForekomst (ForekomstID, RuteID, dato) VALUES 
                            (1, 1, '2023-03-04'),
                            (2, 2, '2023-03-04'),
                            (3, 3, '2023-03-04'),
                            (4, 1, '2023-04-04'),
                            (5, 2, '2023-04-04'),
                            (6, 3, '2023-04-04')
                            """
    
    inngaarIrute_query = """INSERT INTO InngaarIRute (RuteID, DelstrekningsID) VALUES
                            (1, 1),(1, 2),(1, 3),(1, 4),(1, 5),
                            (2, 1),(2, 2),(2, 3),(2, 4),(2, 5),
                            (3, 1),(3, 2),(3, 3)"""
    
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

    c.execute(inngaarIrute_query)
    c.execute("""SELECT * FROM SitteVogn""")
    sete_query ="INSERT INTO Sete (OperatorNavn, VognID, SeteID) VALUES "
    sitteVogner = c.fetchall()
    for vognNr, vogn in enumerate(sitteVogner):
        operator = vogn[0]
        vognID = vogn[1]
        antallRader = vogn[2]
        seterPerRad = vogn[3]
        for seteID in range(antallRader*seterPerRad):
            if (seteID == 0) and (vognNr == 0):
                sete_query+= f"('{operator}',{vognID},{seteID+1})"
            else:
                sete_query+= f", ('{operator}',{vognID},{seteID+1})"
    c.execute(sete_query)

    c.execute("""SELECT * FROM SoveVogn""")
    seng_query ="INSERT INTO Seng (OperatorNavn, VognID, SengeID, KupeNr) VALUES "
    soveVogner = c.fetchall()
    for vognNr, vogn in enumerate(soveVogner):
        sengerPrKupee = 2
        operator = vogn[0]
        vognID = vogn[1]
        antallKupeer = vogn[2]
        for sengeID in range(antallKupeer*sengerPrKupee):
                kupeeNr = 1 + sengeID//sengerPrKupee
                if (sengeID == 0) and (vognNr == 0):
                    seng_query+= f"('{operator}',{vognID},{sengeID+1},{kupeeNr})"
                else:
                    seng_query+= f", ('{operator}',{vognID},{sengeID+1},{kupeeNr})"
    c.execute(seng_query)
    
    c.execute("pragma foreign_keys = ON")
    c.execute(f"INSERT INTO Billett VALUES ({1},{1})")
    c.execute(f"INSERT INTO BillettOmfatter VALUES ({1},{1},{3})")
    c.execute(f"INSERT INTO SitteBillett VALUES ({1},{1},'{'SJ'}',{1},{8})")
    c.execute(f"INSERT INTO SitteBillett VALUES ({1},{1},'{'SJ'}',{1},{9})")
    c.execute(f"INSERT INTO SitteBillett VALUES ({1},{1},'{'SJ'}',{1},{10})")

    c.execute(f"INSERT INTO Billett VALUES ({3},{2})")
    c.execute(f"INSERT INTO BillettOmfatter VALUES ({3},{2},{2})")
    c.execute(f"INSERT INTO SoveBillett VALUES ({3},{2},'{'SJ'}',{5},{2})")
    c.execute(f"INSERT INTO SoveBillett VALUES ({3},{2},'{'SJ'}',{5},{4})")
    c.execute(f"INSERT INTO SoveBillett VALUES ({3},{2},'{'SJ'}',{5},{7})")
    conn.commit()
    conn.close()

# Main program to run
def menu():
    print("Dette er en database over jernbanen i Norge\n")
    print("0. Avslutt program")
    print("1. Finn tidspunkt på togruter som passer en stasjon en gitt ukedag")
    print("2. Finn togruter som går mellom to stasjoner på et tidspunkt og dag")
    print("3. Registrer ny kunde")
    print("4. Kjøp billetter til en togrute")
    print("5. Vis fremtidige reiser\n")
    num = -1
    while num != 0:
        num = input("Skirv inn tallet på operasjonen du ønsker å utføre: ")
        match num:
            case "0":
                break
            case "1":
                date = input("Dato (YYYY-DD-MM): ")
                stasjon1 = input("Startstasjon: ")
                stasjon2 = input("Endestasjon: ")
                search_routes(date, stasjon1, stasjon2)
            case "2":
                stasjon = input ("Hvilken stasjon vil du sjekke? ")
                ukedag = input("Hvilken ukedag? ")
                get_togrute_info(stasjon,ukedag)
            case "3":
                print("KUNDEREGISTRERING\n")
                navn = input("Navn: ")
                epost = input("Epost: ")
                tlf = input("Telefon: ")
                new_user(navn,epost,tlf)
            case "4":
                print("Denne funksjonaliteten støttes ikke enda")
            case "5":
                print("Denne funksjonaliteten støttes ikke enda")
            case _:
                print("Ugyldig input")


# Task c)
def get_togrute_info(stasjon,day):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()
    
    #Check if the stasjon exists by reading from the TABLE Stasjon
    c.execute("SELECT * FROM Stasjon WHERE navn = ?", (stasjon,))
    if c.fetchone() is None:
        print("Stasjonen finnes ikke")
        return
    
    #Check if the ukedag exists by reading from the TABLE Rutedag
    c.execute("SELECT * FROM Rutedag WHERE ukedag = ?", (day,))
    if c.fetchone() is None:
        print("Ukedagen finnes ikke")
        return
    
    c.execute("""SELECT RuteID FROM (RuteTabell INNER JOIN Rutedag USING (RuteID) ) WHERE RuteDag.ukedag = ? and RuteTabell.StasjonsNavn = ? """, (day, stasjon))
    ruter = c.fetchall()

    print("Følgende ruter går fra", stasjon, "på", day + "er:")

    for rute in ruter:
        c.execute("SELECT * FROM Rute WHERE RuteID = ?", (rute[0],))
        ruteinfo = c.fetchall()
        print("Rute: ", ruteinfo[0][1], ruteinfo[0][2], ruteinfo[0][3], ruteinfo[0][4], ruteinfo[0][5])


    conn.close()


# Task d)
def search_routes(date, stasjon1, stasjon2):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    year, day, month = map(int, date.split('-'))
    stasjoner = [stasjon1, stasjon2]
    
    #Check if the stasjon exists by reading from the TABLE Stasjon
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

# Task e)
def new_user(name,email,tlf):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    c.execute("pragma foreign_keys = ON")
    c.execute("SELECT COUNT(*) FROM Kunde")
    antall = c.fetchone()
    newKundeNr = antall[0] + 1


    c.execute("INSERT INTO Kunde VALUES (?,?,?,?)",(newKundeNr,email,name,tlf))

    conn.commit()
    
    print(f"Kunde {newKundeNr}: {name}, {email}, {tlf}")

    conn.close()

# task h)
def future_trips(kundeNr, email):
    var = email

# task g)
def get_delstrekningsIDer(startStasjon, endeStasjon):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()
    # hent alle Delstrekninger som må besøkes for å komme seg fra startstasjon til endestasjon, og hvilken retning det svarer til (MED/MOT).
    c.execute(f"SELECT DelstrekningsID, startStasjon, endeStasjon FROM Delstrekning")
    alle_delstrekninger = c.fetchall()
    delstrekningsIDer = []
    retning = "MED"
    class Found(Exception): pass
    try:
        ny_startStasjon = startStasjon
        for iteration in range(len(alle_delstrekninger)):
            for delstrekning in alle_delstrekninger:
                strekningsID = delstrekning[0]
                start = delstrekning[1]
                slutt = delstrekning[2]
                if ny_startStasjon == start:
                    delstrekningsIDer.append(strekningsID)
                    if endeStasjon == slutt:
                        raise Found
                    ny_startStasjon = slutt

        retning = "MOT"
        delstrekningsIDer = []
        ny_startStasjon = startStasjon
        for iteration in range(len(alle_delstrekninger)):
            for delstrekning in alle_delstrekninger:
                strekningsID = delstrekning[0]
                start = delstrekning[2]
                slutt = delstrekning[1]
                if ny_startStasjon == start:
                    delstrekningsIDer.append(strekningsID)
                    if endeStasjon == slutt:
                        raise Found
                    ny_startStasjon = slutt

        print(f"There is no way to get from {startStasjon} to {endeStasjon}. Sorry!\n")
        conn.close()
        return [], "MED"
    except Found:
        conn.close()
        return delstrekningsIDer, retning


def get_ruter(delstrekningsIDer, retning, dato):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()
    mulige_ruter_sporring = f"""SELECT DISTINCT RuteID
        FROM InngaarIRute
        WHERE RuteID NOT IN (SELECT RuteID WHERE DelstrekningsID NOT IN ({", ".join(delstrekningsIDer)})) 
        AND RuteID IN (SELECT RuteID from Rute WHERE Retning = '{retning}')"""
    c.execute(mulige_ruter_sporring)
    mulige_ruter = [str(Rute[0]) for Rute in c.fetchall()]
    conn.close()
    return mulige_ruter

def get_ruteforekomster(ruter, dato):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()
    mulige_ruteforekomster_sporring = f"""SELECT ForekomstID
    FROM RuteForekomst
    WHERE dato = '{dato}'
    AND RuteID IN ({", ".join(ruter)})"""
    c.execute(mulige_ruteforekomster_sporring)
    mulige_ruteforekomster = [str(Rute[0]) for Rute in c.fetchall()]
    conn.close()
    return mulige_ruteforekomster
  

def get_available_seats(startStasjon, endeStasjon, dato):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    delstrekningsIDer, retning = get_delstrekningsIDer(startStasjon,endeStasjon)
    if not delstrekningsIDer:
        return
    
    mulige_ruter = get_ruter(delstrekningsIDer,retning,dato)
    if not mulige_ruter:
        print(f"No routes exist between {startStasjon} and {endeStasjon}")
        return
    
    mulige_ruteforekomster = get_ruteforekomster(mulige_ruter, dato)
    if not mulige_ruteforekomster:
        print(f"There exists no routes between the given stations on the date: {dato}\n")
        return
    
    # sjekk om det er ledige sittebilletter på denne ruteforekomsten denne dagen
    
    ruteforekomstDict = {}
    for ruteforekomst in mulige_ruteforekomster:
        ledige_seter_sporring = \
        f"""SELECT DISTINCT OperatorNavn, VognID, SeteID
            FROM Sete
            WHERE (OperatorNavn, VognID, SeteID) NOT IN (SELECT OperatorNavn, VognID, SeteID 
                FROM Sete NATURAL JOIN SitteBillett NATURAL JOIN BillettOmfatter
                WHERE ForekomstID = {ruteforekomst}
                AND DelstrekningsID IN ({", ".join(delstrekningsIDer)}))
            AND (OperatorNavn, VognID, SeteID) IN (SELECT OperatorNavn, VognID, SeteID 
                FROM Rute NATURAL JOIN RuteForekomst NATURAL JOIN DelAvTog
                WHERE ForekomstID = {ruteforekomst})
        """
        print(ledige_seter_sporring)
        c.execute(ledige_seter_sporring)
        ledige_seter = c.fetchall()
        ruteforekomstDict[ruteforekomst] = ledige_seter
    
    
    for ruteforekomst, seter in ruteforekomstDict.items():
        klokkeslett_sporring = f"SELECT DISTINCT tid FROM RuteTabell NATURAL JOIN RuteForekomst WHERE ForekomstID = {ruteforekomst} AND StasjonsNavn = '{startStasjon}'"""
        c.execute(klokkeslett_sporring)
        klokkeslett = c.fetchall()[0][0]
        ledigeSeterString =f"\nLedige seter fra {startStasjon} til {endeStasjon} kl: {klokkeslett} den {dato}:\n"
        for sete in seter:
            ledigeSeterString += f"Operatør: {sete[0]}, Vogn:{sete[1]}, Sete:{sete[2]}\n"
        print(ledigeSeterString)
    conn.close()
    print(ruteforekomstDict)
    return ruteforekomstDict

def get_available_beds(startStasjon, endeStasjon, dato):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    delstrekningsIDer, retning = get_delstrekningsIDer(startStasjon,endeStasjon)
    if not delstrekningsIDer:
        return
    
    mulige_ruter = get_ruter(delstrekningsIDer,retning,dato)
    if not mulige_ruter:
        print(f"No routes exist between {startStasjon} and {endeStasjon}")
        return
    
    mulige_ruteforekomster = get_ruteforekomster(mulige_ruter, dato)
    if not mulige_ruteforekomster:
        print(f"There exists no routes between the given stations on the date: {dato}\n")
        return
    
    ruteforekomstDict = {}
    for ruteforekomst in mulige_ruteforekomster:

        ledige_senger_sporring = \
                f"""SELECT DISTINCT Seng.OperatorNavn, Seng.VognID, Seng.SengeID, KupeNr
        FROM Seng
        WHERE KupeNr NOT IN (SELECT KupeNr FROM Seng NATURAL JOIN SoveBillett NATURAL JOIN RuteForekomst WHERE ForekomstID = {ruteforekomst})
        """
        c.execute(ledige_senger_sporring)
        ledige_senger = c.fetchall()
        ruteforekomstDict[ruteforekomst] = ledige_senger
        for ruteforekomst, senger in ruteforekomstDict.items():
            klokkeslett_sporring = f"SELECT DISTINCT tid FROM RuteTabell NATURAL JOIN RuteForekomst WHERE ForekomstID = {ruteforekomst} AND StasjonsNavn = '{startStasjon}'"""
            c.execute(klokkeslett_sporring)
            klokkeslett = c.fetchall()[0][0]
            ledigeSengerString =f"\nLedige senger fra {startStasjon} til {endeStasjon} kl: {klokkeslett} den {dato}:\n"
            for seng in senger:
                ledigeSengerString += f"Operatør: {seng[0]}, Vogn:{seng[1]}, Kupee:{seng[3]}, Seng:{seng[2]}\n"
            print(ledigeSengerString)
        return ruteforekomstDict
    conn.close()
def book_bed():
    pass

def book_seat():
    pass



#menu()
#These functions will create and add data about the Nordlandsbanen to the database
CREATE_db("sql_prosjektet.sql")
init_db('sql_prosjektet.db')

get_available_seats("Mo i Rana", "Fauske", "2023-03-04")
get_available_seats("Mosjøen", "Fauske", "2023-03-04")
get_available_seats("Mosjøen", "Fauske", "2023-04-04")
get_available_seats("Fauske","Mo i Rana" ,"2023-03-04")
get_available_seats("Mo i Rana","Trondheim" ,"2023-03-04")
get_available_seats("Halla","NTNU" ,"2023-03-04")

print("Her kommer Senger\n\n\n\n")
get_available_beds("Mo i Rana","Mosjøen" ,"2023-03-04")
get_available_beds("Mo i Rana","Trondheim" ,"2023-03-04")
get_available_beds("Mo i Rana","Mosjøen" ,"2023-04-04")
get_available_beds("Mo i Rana","Trondheim" ,"2023-04-04")

