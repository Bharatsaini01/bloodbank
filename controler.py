# import views

# def home():
#     print("Welcome to blood bank ")
#     print('Enter 1 for Login ')
#     print('Enter 2 for Register ')
#     choose_no = int(input("Enter a Number"))
#     if choose_no == 1:
#         username = input('Enter your username')
#         password = input('Enter your password')
#         if views.Login(username,password):
#             print("login successfully")
#             views.create_account()
                
#         else:
#             print("invalid username and password")
#     elif choose_no == 2:
#         username = input('Create your username')
#         password = input('Create your password')
#         if views.Register(username,password):
#             home()

# home()

import models

def user_registration(username,data):
    if models.check_user(username):
        models.add_user(data)
        print("Registration successfully")
    else:
        print("username already exists")

def blood_donate(username,donation_times,data):
    if models.check_user(username):
        print("user not found!,please first Registration ")
    elif donation_times == 1:
        models.add_user_donation(data)
        print("Donation successfully")
    else:
        data = (username,blood_group,donation_times,donation_date,predonation_date,username)
        models.update_user_donation(data)
        print("Donation successfully")

def blood_receive(username,check,donation_times,receive_times,data):
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

def user_info(data):
    for i in data:
        user_id,name,username,password,role = i
        print(user_id,"            ",name,"            ",username,"            ",role)

def donation_info(data):
    for i in data:
        username,blood_group,donation_times,donation_date,last_donation_date = i
        print(username,"            ",blood_group,"                 ",donation_times,"                       ",donation_date,"                  ",last_donation_date)

def receive_info(data):
    for i in data:
        username,blood_group,receive_times,receive_date,last_receive_date = i
        print(username,"            ",blood_group,"                  ",receive_times,"                         ",receive_date,"                   ",last_receive_date)


