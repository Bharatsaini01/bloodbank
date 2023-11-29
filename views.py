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

import models
import datetime

def heading():
    print("welcome to blood bank")
    print("Enter 1 for Log in")

def admin_func():
    print("Enter 1 for User Registration")
    print("Enter 2 for Blood Donate")
    print("Enter 3 for Blood receive")
    print("Enter 4 for All Users Information")
    print("Enter 5 for Delete User")
    print("Enter 6 for User Donation Information")
    print("Enter 7 for User Receive Information")


def user_func():
    print("Enter 1 for Your Information")

def user_choice(choice):
    if choice == '1':
       user_info()    
    
def admin_choice(choice):
    if choice == '1':
        user_registration()
    elif choice == '2':
        blood_donate()
    elif choice == '3':
        blood_receive()
    elif choice == '4':
        users_info()
    elif choice == '5':
        delete_user()
    elif choice == '6':
        donation_info()
    elif choice == '7':
        receive_info()
    else:
        print("Invalid choice")

def user_registration():
    '''role 1 for user
       role 2 for admin '''
    name = input("Enter your name : ")
    username = input("Create username : ")
    password = input("Create password : ")
    role = input("Enter role : ")
    data = (name,username,password,role)
    if models.check_user(username):
        models.add_user(data)
        print("Registration successfully")
    else:
        print("username already exists")

def blood_donate():
    username = input("Enter username : ")
    blood_group = input("Enter blood group : ")
    donation_times,predonation_date = models.get_donation_times_and_pre_donation_date(username)
    donation_date = datetime.datetime.now().date()
    data = (username,blood_group,donation_times,donation_date,predonation_date)
    if models.check_user(username):
        print("user not found!,please first Registration ")
    elif donation_times == 1:
        models.add_user_donation(data)
        print("Donation successfully")
    else:
        data = (username,blood_group,donation_times,donation_date,predonation_date,username)
        models.update_user_donation(data)
        print("Donation successfully")

def blood_receive():
    username = input("Enter username : ")
    blood_group = input("Enter blood group : ")
    donation_times,predonation_date = models.get_donation_times_and_pre_donation_date(username)
    receive_times,prereceive_date = models.get_receive_times_and_pre_receive_date(username)
    receive_date = datetime.datetime.now().date()
    check = donation_times - receive_times
    data = (username,blood_group,receive_times,receive_date,prereceive_date)
    if models.check_user(username):
        print("user not found!,please first Registration ")
    elif check == 0 and donation_times>=1:
        print("You already max receive blood")
    elif receive_times == 1:
        models.blood_receive(data)
        print("Receive successfully")
    else:
        data = (username,blood_group,receive_times,receive_date,prereceive_date,username)
        models.update_user_receive(data)
        print("Receive successfully")

def users_info():
    data = models.users_info()
    print("user id          name            username            role ")
    for i in data:
        user_id,name,username,password,role = i
        print(user_id,"            ",name,"            ",username,"            ",role)

def delete_user():
    username = input("Enter username : ")
    models.delete_user(username)
    print("User delete successfully")

def donation_info():
    username= input("Enter username : ")
    data = models.donation_info(username)
    print("Username          Blood Group            Donation Times           Donation Date            Last Donation Date ")
    for i in data:
        username,blood_group,donation_times,donation_date,last_donation_date = i
        print(username,"            ",blood_group,"                 ",donation_times,"                       ",donation_date,"                  ",last_donation_date)

def receive_info():
    username= input("Enter username : ")
    data = models.receive_info(username)
    print("Username          Blood Group            Receive Times           Receive Date            Last Receive Date ")
    for i in data:
        username,blood_group,receive_times,receive_date,last_receive_date = i
        print(username,"            ",blood_group,"                  ",receive_times,"                         ",receive_date,"                   ",last_receive_date)

def user_info():
    username = input("Enter your username : ")
    data = models.user_info(username)
    print("user id          name            username            role ")
    user_id,name,username,password,role = data[0]
    print(user_id,"            ",name,"            ",username,"            ",role)

def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    role = models.Check_user_validation(username,password)
    if role :
        if role == 2:
            print("log in successfully")
            admin_func()
            choice = input("Enter your choice : ")
            admin_choice(choice)
        else:
            print(role)
            print("log in successfully")
            user_func()
            choice = input("Enter your choice : ")
            user_choice(choice)

    else:    
        print("Invalid username or password")