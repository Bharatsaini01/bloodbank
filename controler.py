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

import views

def blood_bank():
    views.heading()
    n = input("Enter Your Choice : ")
    if n == '1':
        views.login()
    else:
        print("invalid choice")
   
blood_bank()