import sqlite3
import os
import datetime 
from datetime import datetime, timedelta



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

    (3, 'SJ', 4, 1)
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
    
    """ c.execute("pragma foreign_keys = ON")
    c.execute(f"INSERT INTO Billett VALUES ({1},{1})")
    c.execute(f"INSERT INTO BillettOmfatter VALUES ({1},{1},{3})")
    c.execute(f"INSERT INTO SitteBillett VALUES ({1},{1},'{'SJ'}',{1},{8})")
    c.execute(f"INSERT INTO SitteBillett VALUES ({1},{1},'{'SJ'}',{1},{9})")
    c.execute(f"INSERT INTO SitteBillett VALUES ({1},{1},'{'SJ'}',{1},{10})")

    c.execute(f"INSERT INTO Billett VALUES ({3},{2})")
    c.execute(f"INSERT INTO BillettOmfatter VALUES ({3},{2},{2})")
    c.execute(f"INSERT INTO SoveBillett VALUES ({3},{2},'{'SJ'}',{5},{2})")
    c.execute(f"INSERT INTO SoveBillett VALUES ({3},{2},'{'SJ'}',{5},{4})")
    c.execute(f"INSERT INTO SoveBillett VALUES ({3},{2},'{'SJ'}',{5},{7})") """
    conn.commit()
    conn.close()


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

    print("Følgende ruter passerer ", stasjon, "på", day + "er:")
    print("RuteID  -  Retning  - Fra -  Til")
    for rute in ruter:
        c.execute("SELECT * FROM Rute WHERE RuteID = ?", (rute[0],))
        ruteinfo = c.fetchall()
        print(ruteinfo[0][1], ruteinfo[0][2], ruteinfo[0][3], "-",ruteinfo[0][4], ruteinfo[0][5])


    conn.close()

def add_one_day(date_str):
    date = datetime.strptime(date_str, "%Y-%d-%m")

    new_date = date + timedelta(days=1)

    if new_date.month != date.month:
        new_date = new_date.replace(day=1)
    if new_date.year != date.year:
        new_date = new_date.replace(month=1, day=1)

    new_date_str = new_date.strftime("%Y-%d-%m")

    return new_date_str


# Task d)
def search_routes(date_str, stasjon1, stasjon2):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    date_str2 = add_one_day(date_str)

    # Check if the stasjon exists by reading from the TABLE Stasjon
    c.execute(f"SELECT * FROM Rute WHERE startStasjon = '{stasjon1}'")
    ret1 = c.fetchone()
    if ret1 is None:
        print("Oppgitt startsasjon er ikke en startstasjon blant tilgjengelige togruter.")
        return
    c.execute(f"SELECT * FROM Rute WHERE endeStasjon = '{stasjon2}'")
    ret2 = c.fetchone()
    if ret2 is None:
        print("Oppgitt endestasjon er ikke en endestasjon blant tilgjengelige togruter.")
        return

    # Find all routes from stasjon1 to stasjon2 on the given date

    # first find all ruteforekomster
    c.execute(f"""SELECT DISTINCT RuteID,startStasjon,endeStasjon,dato,tid 
                FROM (RuteForekomst NATURAL JOIN Rute) NATURAL JOIN RuteTabell
                WHERE (RuteForekomst.dato = '{date_str}' OR RuteForekomst.dato = '{date_str2}') AND RuteTabell.StasjonsNavn = '{stasjon1}' AND Rute.endeStasjon = '{stasjon2}'
                ORDER BY RuteForekomst.dato,RuteTabell.tid""")
    rows = c.fetchall()
    if not rows:
        print("Togruten går ikke den ønskede dagen eller neste")
    else:
        for row in rows:
            print(f"Rute {row[0]}: {row[1]}-{row[2]} {row[3]} kl. {row[4]}")

    conn.close()


# Task e)



# Task e)
def new_user(name,email,tlf):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    c.execute("pragma foreign_keys = ON")
    c.execute("SELECT COUNT(*) FROM Kunde")
    antall = c.fetchone()
    newKundeNr = antall[0] + 1

    #Some kind of check as to if the user already exists
    c.execute("SELECT * FROM Kunde WHERE epostAddr = ?", (email,))
    exists_already = c.fetchall()
    if len(exists_already) >= 1:
        print("Kunden finnes allerede")
        return

    c.execute("INSERT INTO Kunde VALUES (?,?,?,?)",(newKundeNr,email,name,tlf))

    conn.commit()
    
    print(f"Kunde {newKundeNr}: {name}, {email}, {tlf}")

    conn.close()

# task h)

def get_seat(billettID,forekomstID):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    seteInfo = c.execute(
        f"""
        SELECT SitteBillett.SeteID,SitteBillett.VognID,SitteBillett.OperatorNavn,DelAvTog.NummerIRekke
        FROM SitteBillett INNER JOIN DelAvTog USING(VognID,OperatorNavn)
        WHERE billettID = '{billettID}' AND ForekomstID = '{forekomstID}'
        """)
    
    res = seteInfo.fetchall()
    conn.close()
    return res

def get_bed(billettID,forekomstID):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    seteInfo = c.execute(
        f"""
        SELECT SoveBillett.SengeID,SoveBillett.VognID,SoveBillett.OperatorNavn,DelAvTog.NummerIRekke
        FROM SoveBillett INNER JOIN DelAvTog USING(VognID,OperatorNavn)
        WHERE billettID = '{billettID}' AND ForekomstID = '{forekomstID}'
        """)
    
    res = seteInfo.fetchall()
    conn.close()
    return res

def get_ticket(email):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    ticketInfo = c.execute(
        f"""
        SELECT DISTINCT Bestilling.OrdreNr,Bestilling.ForekomstID,Bestilling.billettID
        FROM ((Kunde NATURAL JOIN KundeOrdre) NATURAL JOIN Bestilling)
        WHERE Kunde.epostAddr = '{email}'
        """)
    res = ticketInfo.fetchall()
    conn.close()
    return res

def get_rute_info(email):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    sit_q = c.execute("""
    SELECT billettID 
    FROM SitteBillett
    """)
    sit_q_res = sit_q.fetchall()

    tripInfo = []
    for ticket in get_ticket(email):
        query = c.execute(f"""
        SELECT Rute.RuteID, RuteForekomst.dato
        FROM RuteForekomst NATURAL JOIN Rute
        WHERE RuteForekomst.ForekomstID = '{ticket[1]}'
        ORDER BY RuteForekomst.dato
        """)
        # Sjekker om billettID tilhører en sittebillett, i så fall lages en ny tuppel ele som inneholder
        # setet (seteID, vognID, operatørNavn) og vognNr i det første del, og ruteID og forekomsDato i andre del 
        res = query.fetchone()
        if res[2] in sit_q_res:
            ele = (get_seat(res[2],res[1]),res)
            tripInfo.append(ele)
        else:
            ele = (get_bed(res[2],res[1]),res)
            tripInfo.append(ele)
        

    conn.close()

    return tripInfo


    """ 
    def future_trips(email):
    conn = sqlite3.connect('sql_prosjektet.db')
    c = conn.cursor()

    rute_info = get_rute_info(email)
    seat_info = get_seat()
    bed_info = get_bed()
    info = []

    print("Her er dine billetter:\n")
    
    for i in range(len(get_rute_info(email))):
        if i == True:
            print(f"{ticket[1]}: Rute nummer {ticket[0]} i vogn {get_seat(ticket[0])}")
            beds.append(get_seat(ticket[2][1]))
            seats.append(get_bed(ticket[2][1]))
    

    
    customer = c.execute(
    f'''
    SELECT DISTINCT Kunde.KundeNr, 
    FORM (((Kunde NATURAL JOIN KundeOrdre) NATURAL JOIN Bestilling) NATURAL JOIN BillettOmfatter) NATURAL JOIN RuteForekomst) NATURAL JOIN Delstrekning) NATURAL JOIN Rute)
    WHERE Kunde.epostAddr = '{email}'
    )'''
    """



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
        #print(ledige_seter_sporring)
        c.execute(ledige_seter_sporring)
        ledige_seter = c.fetchall()
        ruteforekomstDict[ruteforekomst] = ledige_seter
    
    
    for ruteforekomst, seter in ruteforekomstDict.items():
        klokkeslett_sporring = f"SELECT DISTINCT tid FROM RuteTabell NATURAL JOIN RuteForekomst WHERE ForekomstID = {ruteforekomst} AND StasjonsNavn = '{startStasjon}'"""
        c.execute(klokkeslett_sporring)
        klokkeslett = c.fetchall()[0][0]
        ledigeSeterString =f"\nLedige seter fra {startStasjon} til {endeStasjon} kl: {klokkeslett} den {dato}: med ruteforekomst: {ruteforekomst}\n"
        for sete in seter:
            ledigeSeterString += f"{sete[0]}, Vogn:{sete[1]}, Sete:{sete[2]}\n"
        print(ledigeSeterString)
    conn.close()
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
            ledigeSengerString =f"\nLedige senger fra {startStasjon} til {endeStasjon} kl: {klokkeslett} den {dato} med ruteforekomst: {ruteforekomst}\n"
            for seng in senger:
                ledigeSengerString += f"Operatør: {seng[0]}, Vogn:{seng[1]}, Kupee:{seng[3]}, Seng:{seng[2]}\n"
            print(ledigeSengerString)
        return ruteforekomstDict
    conn.close()


# Oppgave g) - står ikke eksplisitt at kunden skal oppgi hvilken dato den ønsker biletter på men det har vi antatt
def ticket_purchase(antallbiletter, kundenr, startstasjon, endestasjon, dato):
    try:
        #Check if the customer exists
        conn = sqlite3.connect('sql_prosjektet.db')
        c = conn.cursor()
        c.execute("pragma foreign_keys = ON")

    
        kunde_spørring = f"SELECT * FROM Kunde WHERE KundeNr = {kundenr}"
        c.execute(kunde_spørring)
        kundeinfo = c.fetchall()
        if not kundeinfo:
            print("Kunden finnes ikke")
            return
        
        #get the current date and time
        now = datetime.now()

      
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        max_ordrenr = f"SELECT Count(*) FROM KundeOrdre"
        c.execute(max_ordrenr)
        max_ordrenr = c.fetchall()[0][0]

        kundeordre = f"INSERT INTO KundeOrdre (OrdreNr, KundeNr, datoForBestilling, tidspunktForBestilling, antallBilletter) VALUES ({max_ordrenr+1}, {kundenr}, '{current_date}', '{current_time}', {antallbiletter})"
        c.execute(kundeordre)
        

        print("Velg hvilken billetttype du ønsker å kjøpe")
        print("1: Sittebillett")
        print("2: Sovebillett")
        
        valg = input("Hva slags billett ønsker du å kjøpe? ")
        
        
        if valg == "1":
            biletter_dict = get_available_seats(startstasjon, endestasjon, dato)
            if not biletter_dict:
                return
            
            ruteforekomst = input("Hvilken ruteforekomst ønsker du å kjøpe billett til?")

            for i in range(antallbiletter):
                valg = input("Hvilken vogn, sete ønsker du? Skriv inn på følgende vis: Vogn, Sete ")

                vogn, sete = valg.split(",")
                vogn = vogn.strip()
                sete = sete.strip()
                #Sjekk om setet er ledig
                operator = biletter_dict[ruteforekomst][0][0]
            
                if (operator, int(vogn), int(sete)) in biletter_dict[ruteforekomst]:
                    print("Setet er ledig")

                    #Legg inn billetten i databasen
                    #Finn antall biletter i tabellen
                    c.execute("SELECT Count(*) FROM Billett")
                    id = c.fetchall()[0][0] + 1
                    insert_billettt = f"INSERT INTO Billett VALUES ({ruteforekomst}, {id})"
                    c.execute(insert_billettt)

                    ##Legge inn i sittebilett
                    sittebillett_insert = f"INSERT INTO SitteBillett VALUES ({ruteforekomst}, {id}, '{operator}', '{vogn}', '{sete}')"
                    c.execute(sittebillett_insert)
                    
                    #Fikse kundehos her
                    kundehos_query = f"SELECT * FROM KundeHos WHERE KundeNr = {kundenr} AND OperatorNavn = '{operator}'"
                    #Check number of rows in kundehos
                    c.execute(kundehos_query)
                    kundehos = c.fetchall()
                    if not kundehos:
                        #Add the customer to the operator
                        kundehos_insert = f"INSERT INTO KundeHos VALUES ({kundenr}, '{operator}')"
                        c.execute(kundehos_insert)

                   

                    c.execute(f"INSERT INTO Bestilling VALUES ({max_ordrenr+1}, {ruteforekomst}, {id})")

                    #Få alle delstrekningsIDer denne biletten gjelder for
                    delstrekningsIDer, retning = get_delstrekningsIDer(startstasjon, endestasjon)
                    for delstrekningsID in delstrekningsIDer:
                        ##Her skal det legges inn i Bilettomfatter
                        bilettomfatter_insert = f"INSERT INTO BillettOmfatter VALUES ({ruteforekomst}, {id}, {int(delstrekningsID)})"
                        c.execute(bilettomfatter_insert)
                print("Gratulerer med vel gjennomført kjøp av sittebillett")
        elif valg == "2":
            ##Fiks sengene 
            biletter_dict = get_available_beds(startstasjon, endestasjon, dato)

            rutestring = f"Hvilken ruteforekomst ønsker du å kjøpe billett på?"
            ruteforekomst = input(rutestring)

            for i in range(antallbiletter):
                valg = input("Hvilken vogn, kupee, seng ønsker du? Skriv inn på følgende vis: Vogn, Kupee, Seng ")
                vogn, kupe, seng = valg.split(",")
                vogn = vogn.strip()
                kupe = kupe.strip()
                seng = seng.strip()

                operator = biletter_dict[ruteforekomst][0][0]
                if (operator, int(vogn), int(seng), int(kupe)) in biletter_dict[ruteforekomst]:
                    print("Sengen er ledig")
                    c.execute("SELECT MAX(billettID) FROM Billett")
                    id = c.fetchone()[0] + 1
                    insert_billettt = f"INSERT INTO Billett VALUES ({ruteforekomst}, {id})"
                    c.execute(insert_billettt)

                    sovebillett_insert = f"INSERT INTO SoveBillett VALUES ({ruteforekomst}, {id}, '{operator}', '{vogn}','{seng}')"
                    c.execute(sovebillett_insert)

                    #Fikse kundehos her
                    kundehos_query = f"SELECT * FROM KundeHos WHERE KundeNr = {kundenr} AND OperatorNavn = '{operator}'"
                    #Check number of rows in kundehos
                    c.execute(kundehos_query)
                    kundehos = c.fetchall()
                    if not kundehos:
                        #Add the customer to the operator
                        kundehos_insert = f"INSERT INTO KundeHos VALUES ({kundenr}, '{operator}')"
                        c.execute(kundehos_insert)

                    ##Legge inn i bestilling
                    c.execute("SELECT Count(*) FROM Bestilling")
                    
                    max_bestilling = c.fetchall()[0][0]
                    c.execute(f"INSERT INTO Bestilling VALUES ({max_ordrenr+1}, {ruteforekomst}, {id})")
                    
                    #Få alle delstrekningsIDer denne biletten gjelder for

                    # get ruteid from forekomstid
                    ruteid = f"SELECT RuteID FROM RuteForekomst WHERE ForekomstID = {ruteforekomst}"
                    c.execute(ruteid)
                    ruteid = c.fetchall()[0][0]


                    samtlige_delstrekninger = f"SELECT DelstrekningsID FROM InngaarIRute WHERE RuteID = {int(ruteid)} "
                    c.execute(samtlige_delstrekninger)
                    delstrekningsIDer = c.fetchall()
                    for delstrekningsID in delstrekningsIDer:
        
                        bilettomfatter_insert = f"INSERT INTO BillettOmfatter VALUES ({ruteforekomst}, {id}, {int(delstrekningsID[0][0])})"
                        c.execute(bilettomfatter_insert)
                print("Gratulerer med vel gjennomført kjøp av sovebillett")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Noe gikk galt : {e}")
        conn.close()



def menu():
    print("Dette er en database over jernbanen i Norge\n")
    print("0. Avslutt program")
    print("1. Finn togruter som passer en stasjon en gitt ukedag")
    print("2. Finn togruter som går mellom to stasjoner på et tidspunkt og dag")
    print("3. Registrer ny kunde")
    print("4. Kjøp billetter til en togrute")
    print("5. Vis fremtidige reiser\n")
    num = -1

    while num != 0:
        match num:
            case "0":
                break
            case "1":
                print("FINN TOGRUTER SOM PASSER EN STASJON EN GITT UKEDAG\n")
                stasjon = input ("Hvilken stasjon vil du sjekke? ")
                ukedag = input("Hvilken ukedag? ")
                print("")
                get_togrute_info(stasjon,ukedag)
            case "2":
                print("FINN TOGRUTER SOM GÅR MELLOM TO STASJONER PÅ ET TIDSPUNKT OG DAG\n")
                startStasjon = input("Fra hvilken stasjon vil du reise? ")
                endeStasjon = input("Til hvilken stasjon vil du reise? ")

                dato = input("Hvilken dato? (YYYY-MM-DD) ")
                print("")
                search_routes(startStasjon,endeStasjon,dato)

            case "3":
                print("KUNDEREGISTRERING\n")
                navn = input("Navn: ")
                epost = input("Epost: ")
                tlf = input("Telefon: ")
                new_user(navn,epost,tlf)
            case "4":
                print("KJØP BILLETTER TIL EN TOGRUTE\n")
                startStasjon = input("Fra hvilken stasjon vil du reise? ")
                endeStasjon = input("Til hvilken stasjon vil du reise? ")
                dato = input("Hvilken dato? (YYYY-DD-MM) ")
                antallBiletter = input("Hvor mange biletter vil du kjøpe? ")
                
                kundenr = input("Hvilket kundenr vil du bruke? ")
                ticket_purchase(int(antallBiletter), int(kundenr), startStasjon, endeStasjon, dato)



            case "5":
                print("Denne funksjonaliteten støttes ikke enda")
            case "-1":
                print("Ugyldig input")

        num = input("Velg et alternativ: ")


if __name__ == "__main__":
    #CREATE_db("sql_prosjektet.sql")
    #init_db('sql_prosjektet.db')

    menu()

    res = get_seat(1, 3)
    print(res)
    res2 = get_bed("mail", 2)
    print(res2)
