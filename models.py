
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

import sqlite3

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

cursur.execute("""CREATE TABLE IF NOT EXISTS BLOOD_DONATION
               (
                USERNAME TEXT NOT NULL UNIQUE,
                BLOOD_GROUP TEXT NOT NULL,
                DONATION_TIMES INT NOT NULL,
                DONATION_DATE DATE NOT NULL,
                LAST_DONATION_DATE DATE                
               )""")

print("successfully create table")
#cursur.execute("INSERT INTO USERS(NAME,USERNAME,PASSWORD,ROLE) VALUES('Bharat','bharat','bharat123',2)")

def Check_user_validation(username,password):
    cursur.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = (?)",[username])
    Password = cursur.fetchone()
    if password in Password :
        return True
    return False

def check_user(username):
    cursur.execute("SELECT * FROM USERS WHERE USERNAME = (?)",[username])
    data = cursur.fetchone()
    if data:
        connection.close()
        return False
    return True

def add_user(data):
    cursur.execute("INSERT INTO USERS(NAME,USERNAME,PASSWORD,ROLE) VALUES(?,?,?,?)",data)
    connection.commit()

def get_donation_times(username):
    cursur.execute("SELECT DONATION_TIMES FROM BLOOD_DONATION WHERE USERNAME = (?)",[username])
    data = int(cursur.fetchone())
    if data:
        return data
    return 0

print(get_donation_times("ritik"))

connection.commit()


