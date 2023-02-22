import sqlite3
from sqlite3 import Error
from os.path import exists


def create_database(db_file):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Database connected successfully!")
        print("SQLite version: " + sqlite3.version)
    except Error as e:
        print(f"An error has occured: {e}")
    finally:
        if connection:
            connection.close()


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(f"An error has occured: {e}")

    return connection


def create_table(connection, sql_statement):
    try:
        c = connection.cursor()
        c.execute(sql_statement)
    except Error as e:
        print(f"An error has occured: {e}")


if __name__ == '__main__':
    database = "komis.sqlite"

    # Create database if it doesnt; exist
    if not exists(database):
        create_database(database)

    # SQL statements for creating tables
    sql_create_samochod_table = """ CREATE TABLE IF NOT EXISTS samochod (
                                        id_s integer PRIMARY KEY,
                                        marka text NOT NULL,
                                        model text NOT NULL,
                                        rok_produkcji text NOT NULL,
                                        przebieg integer,
                                        cena real
                                    ); """

    sql_create_klient_table = """ CREATE TABLE IF NOT EXISTS klient (
                                      id_k integer PRIMARY KEY,
                                      imie text NOT NULL,
                                      nazwisko text NOT NULL,
                                      tel text,
                                      miasto text NOT NULL
                                  ); """

    sql_create_sprzedaz_table = """ CREATE TABLE IF NOT EXISTS sprzedaz (
                                        id integer PRIMARY KEY,
                                        id_s integer NOT NULL,
                                        id_k integer NOT NULL,
                                        data text,
                                        FOREIGN KEY (id_s) REFERENCES samochod (id_s),
                                        FOREIGN KEY (id_k) REFERENCES klient (id_k)
                                    ); """

    # Create a database connection
    connection = create_connection(database)

    # Create tables
    if connection is not None:
        create_table(connection, sql_create_samochod_table)
        create_table(connection, sql_create_klient_table)
        create_table(connection, sql_create_sprzedaz_table)
    else:
        print("An error occured while creating the tables.")

    # Insert data into database
    c = connection.cursor()

    c.execute('SELECT id_s FROM samochod WHERE id_s IN (1,2);')
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute('INSERT INTO samochod VALUES(1, "Volvo", "ABC123", "1999", 645120, 32000.0);')
        c.execute('INSERT INTO samochod VALUES(2, "BMW", "DEF456", "2001", 58930, 64000.0);')

    c.execute('SELECT id_k FROM klient WHERE id_k IN (1,2);')
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute('INSERT INTO klient VALUES(1, "Jan", "Kowalski", "+48 986 654 321", "Warszawa");')
        c.execute('INSERT INTO klient VALUES(2, "Barbara", "Kowalska", "+48 098 123 123", "Lublin");')

    c.execute('SELECT id_k FROM sprzedaz WHERE id_k IN (1,2);')
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute('INSERT INTO sprzedaz VALUES(1, 2, 1, "20-08-2012");')
        c.execute('INSERT INTO sprzedaz VALUES(2, 1, 2, "31-10-2020");')

    # Query data from tables
    c.execute("SELECT * FROM samochod")
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.execute("SELECT * FROM klient")
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.execute("SELECT * FROM sprzedaz")
    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()

    try:
        connection.commit()
    except Error as e:
        connection.rollback()
    finally:
        connection.close()
