
import sqlite3
import hashlib

"""
    The purpose of this program is to create the initial database.
    this program is launched before the main/controller 
"""

# file containing the SQLite Database
database = "alumni_db.sq3"
# creating connection to the database
socket = sqlite3.connect(database)
#creating a cursor that will contain the SQL queries to execute
request = socket.cursor()


#creating Tables
request.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
lastname TEXT NOT NULL,
firstname TEXT NOT NULL,
number TEXT,
street TEXT,
zipcode TEXT,
city TEXT,
tel TEXT,
mail TEXT,
photo TEXT
)""")

request.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
login TEXT,
hash TEXT)
""")

request.execute(
    """INSERT INTO users (login, hash) 
    VALUES ("admin",
    "46d67f3083f7c097922e45295137d48e0827ca3484bb27749cbeca5743906203")
    """)


'''
#only for create the hashed password :
a = bytes(input(),"utf-8")
hashed_pwd = hashlib.sha256(a).hexdigest()
print(hashed_pwd)

only for test :
# read the data tables
request.execute("""SELECT login, hash FROM users""")
test = request.fetchall()
for row in test:
    print('login : {0},'' pwd : {1}'.format(row[0], row[1])) 

'''

socket.commit()