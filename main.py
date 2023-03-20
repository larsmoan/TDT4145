import sqlite3




def create_db(filename):
    #Just a dummy name for the database
    db_filename = filename[:-4] + '.db'
    conn = sqlite3.connect(db_filename)

    with open(filename, 'r') as sql_file:
        conn.executescript(sql_file.read())

    conn.close()


