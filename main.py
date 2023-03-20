import sqlite3




def create_db(filename):
    #Just a dummy name for the database
    db_filename = filename[:-4] + '.db'
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
    c.execute(stasjons_query)
    conn.commit()
    conn.close()

create_db("sql_prosjektet.sql")
init_db('sql_prosjektet.db')


