import sqlite3

# connection = sqlite3.connect('BMS.db')
# cursor = connection.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS DONOR
#                (
#                DONOR_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                DONOR_NAME TEXT NOT NULL,
#                BLOOD_GROUP TEXT NOT NULL,
#                MOBILE_NO INT UNIQUE
#                )""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS RECEIVER
#                (
#                RECEIVER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                RECEIVER_NAME TEXT NOT NULL,
#                BLOOD_GROUP TEXT NOT NULL,
#                MOBILE_NO INT UNIQUE
#                ) """)

# cursor.execute("""CREATE TABLE IF NOT EXISTS USERS
#                (
#                REGISTER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                USERNAME VARCHAR(10) UNIQUE NOT NULL,
#                PASSWORD TEXT NOT NULL
#                ) """)

# # cursor.execute("INSERT INTO USERS VALUES(NULL,'BHARAT','BHARAT')")
# connection.commit()

connection = sqlite3.connect('blood bank.db')
print("successfully connect database")
cursur = connection.cursor()

cursur.execute("""CREATE TABLE IF NOT EXISTS USERS
               (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                USERNAME TEXT NOT NULL UNIQUE,
                PASSWORD TEXT NOT NULL,
                ROLE INT NOT NULL DEFAULT 1
               )""")

print("successfully create table")
#cursur.execute("INSERT INTO USERS(NAME,USERNAME,PASSWORD,ROLE) VALUES('Bharat','bharat','bharat123',2)")

def Check_user(username,password):
    Pd = cursur.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = (?)",[username])
    Password = cursur.fetchone()
    print(Password)
    if password == Password :
        return True
    return False

connection.commit()


