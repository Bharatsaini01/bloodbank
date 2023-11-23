# import connector

# def Login(username,password):
#     connector.cursor.execute("SELECT PASSWORD FROM USERS WHERE USERNAME =  '{}'".format(username))
#     PASSWORD = connector.cursor.fetchall()
#     if password in PASSWORD[0]:
#         return True
#     else:
#         return False

# def Register(username,password):
#     if Login(username,password):
#         print('username already access')
#     else:
#         connector.cursor.execute("INSERT INTO USERS VALUES(NULL,'{}','{}')".format(username,password))
#         connector.connection.commit()
#         print('Successfully Register')
#         return True

# def CREATE_DONOR_ACCOUNT():
#     print("Enter Your Details")
#     donor_name =    input("Donor Name  : ")
#     blood_group =   input("Blood Group : ")
#     mobile_no = int(input("Mobile No.  : "))
#     connector.cursor.execute("SELECT MOBILE_NO FROM DONOR WHERE MOBILE_NO = {}".format(mobile_no))
#     MOBILE_NO = connector.cursor.fetchall()
#     if MOBILE_NO == []:
#         MOBILE_NO = [()]
#     if mobile_no in MOBILE_NO[0]:
#         print("This Mobile No. already access")
#     else:
#         connector.cursor.execute("INSERT INTO DONOR VALUES(NULL,'{}','{}','{}')".format(donor_name,blood_group,mobile_no))
#         connector.connection.commit()
#         print('Successfully Create Donor Account')

# def CREATE_RECEIVER_ACCOUNT():
#     print("Enter Your Details")
#     receiver_name =  input("Receiver Name : ")
#     blood_group =    input("Blood Group   : ")
#     mobile_no =  int(input("Mobile No.    : "))
#     connector.cursor.execute("SELECT MOBILE_NO FROM RECEIVER WHERE MOBILE_NO = {}".format(mobile_no))
#     MOBILE_NO = connector.cursor.fetchall()
#     if MOBILE_NO == []:
#         MOBILE_NO = [()]
#     if mobile_no == MOBILE_NO[0]:
#         print("This Mobile No. already access")
#     else:
#         connector.cursor.execute("INSERT INTO RECEIVER VALUES(NULL,'{}','{}','{}')".format(receiver_name,blood_group,mobile_no))
#         connector.connection.commit()
#         print('Successfully Create Receiver Account')

# def create_account():
#     print("Enter 1 for Create donor Account")
#     print("Enter 2 for Create receiver Account")
#     num = int(input("Enter a number: "))
#     if num == 1:
#         CREATE_DONOR_ACCOUNT()
#     elif num == 2:
#         CREATE_RECEIVER_ACCOUNT()
#     else:
#         print("Invailed number")

import connector

def heading():
    print("welcome to blood bank")
    print("Enter 1 for Log in")
    print("Enter 2 for Register")
    
def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if connector.Check_user(username,password) :
        print("log in successfully")
    print("Invalid username and password")