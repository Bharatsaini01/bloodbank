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

cursur.execute("""CREATE TABLE IF NOT EXISTS BLOOD_DONATION
               (
                USERNAME TEXT NOT NULL UNIQUE,
                BLOOD_GROUP TEXT NOT NULL,
                DONATION_TIMES INT NOT NULL,
                DONATION_DATE DATE NOT NULL,
                LAST_DONATION_DATE DATE                
               )""")

cursur.execute("""CREATE TABLE IF NOT EXISTS BLOOD_RECEIVE
               (
                USERNAME TEXT NOT NULL UNIQUE,
                BLOOD_GROUP TEXT NOT NULL,
                RECEIVE_TIMES INT NOT NULL,
                RECEIVE_DATE DATE NOT NULL,
                LAST_RECEIVE_DATE DATE                
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
        return False
    return True

def add_user(data):
    cursur.execute("INSERT INTO USERS(NAME,USERNAME,PASSWORD,ROLE) VALUES(?,?,?,?)",data)
    connection.commit()
    connection.close()

def get_donation_times_and_pre_donation_date(username):
    cursur.execute("SELECT DONATION_TIMES,DONATION_DATE FROM BLOOD_DONATION WHERE USERNAME = (?)",[username])
    data = cursur.fetchall()
    if data:
        data1,data2 = data[0]
        return data1+1,data2
    else:
        return 1,None
    


def add_user_donation(data):
    cursur.execute("INSERT INTO BLOOD_DONATION VALUES(?,?,?,?,?)",data)
    connection.commit()

def update_user_donation(data):
    cursur.execute("UPDATE BLOOD_DONATION SET (USERNAME,BLOOD_GROUP,DONATION_TIMES,DONATION_DATE,LAST_DONATION_DATE)=(?,?,?,?,?) WHERE USERNAME = (?)",data)
    connection.commit()

def get_receive_times_and_pre_receive_date(username):
    cursur.execute("SELECT RECEIVE_TIMES,RECEIVE_DATE FROM BLOOD_RECEIVE WHERE USERNAME = (?)",[username])
    data = cursur.fetchall()
    if data:
        data1,data2 = data[0]
        return data1+1,data2
    else:
        return 1,None
    
def blood_receive(data):
    cursur.execute("INSERT INTO BLOOD_RECEIVE VALUES(?,?,?,?,?)",data)
    connection.commit()

def update_user_receive(data):
    cursur.execute("UPDATE BLOOD_RECEIVE SET (USERNAME,BLOOD_GROUP,RECEIVE_TIMES,RECEIVE_DATE,LAST_RECEIVE_DATE)=(?,?,?,?,?) WHERE USERNAME = (?)",data)
    connection.commit()

def user_info():
    cursur.execute("SELECT * FROM USERS")
    data = cursur.fetchall()
    return data

def delete_user(username):
    cursur.execute("DELETE FROM USERS WHERE USERNAME=(?) ",(username,))
    connection.commit()

connection.commit()


