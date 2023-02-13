import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    
    print("\n Database  user {} connected to MySQL on host {} with database {}",format(config["user"]+","+config["host"]+","+config["database"]))
    
    input("\n\n Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_08_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)


cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name from studio")
movies = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS --")
for studio in movies:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

print()
    
cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name from genre")
movies = cursor.fetchall()
print("-- DISPLAYING Genre RECORDS --")
for genre in movies:
    print("Genre ID: {}\n Genre Name: {}\n".format(genre[0], genre[1]))

cursor = db.cursor()
cursor.execute("SELECT film_name, film_runtime from film where film_runtime < 120")
movies = cursor.fetchall()
print("-- DISPLAYING Short Film RECORDS --")
for film in movies:
    print("Film Name: {}\n Runtime: {}\n".format(film[0], film[1]))
    
cursor = db.cursor()
cursor.execute("SELECT film_name, film_director from film order by film_director ASC")
movies = cursor.fetchall()
print("-- DISPLAYING Director RECORDS in Order --")
for film in movies:
    print("Film Name: {}\n Director: {}\n".format(film[0], film[1]))


db.close() 