import csv, sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def main():
    database = "db.sqlite3"


    conn = create_connection(database)
    cur = conn.cursor()


    # insert movie records
    
    with open('dataset_history_django_features.csv','r', encoding='utf8') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # default delimiter: comma
        to_db = [(col['film_id_allocine'], col['titre'], col['image'],col['genre'], col['date']) for col in dr]

    cur.executemany("""INSERT INTO movies
    				(id, titre, image, genre, date) 
    				VALUES (?, ?, ?, ?, ?);""", to_db)
    conn.commit()
    conn.close()

    # insert boxoffice records
    
    with open('dataset_history_django_features.csv','r', encoding='utf8') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # default delimiter: comma
        to_db = [(col['film_id_allocine'], col['boxoffice']) for col in dr]

    cur.executemany("""INSERT INTO boxoffice
    				(id, boxoffice) 
    				VALUES (?, ?);""", to_db)
    conn.commit()
    conn.close()

    # --------- Other Database ------------ @ TODO

if __name__ == '__main__':
    main()



