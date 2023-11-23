# import models

# def home():
#     print("Welcome to blood bank ")
#     print('Enter 1 for Login ')
#     print('Enter 2 for Register ')
#     choose_no = int(input("Enter a Number"))
#     if choose_no == 1:
#         username = input('Enter your username')
#         password = input('Enter your password')
#         if models.Login(username,password):
#             print("login successfully")
#             models.create_account()
                
#         else:
#             print("invalid username and password")
#     elif choose_no == 2:
#         username = input('Create your username')
#         password = input('Create your password')
#         if models.Register(username,password):
#             home()

# home()

import models
def blood_bank():
    models.heading()
    n = input("Enter Your Choice : ")
    if n == '1':
        models.login()

blood_bank()