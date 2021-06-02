
def login_dr():
    User = input('enter your user: ')

    while not (User.isdigit()) and not (User.islower()):
    User = input('Please Try again')

    ID=input('enter your id: ')
    while not ID.isdigit():
    ID = input('Please Try again')

    User = "moshe123"
    userName = input('enter your user: ')
    if userName != User:
     print('try again')

    Password = "moshe123!"
    if len(Password) > 10 :
    print('try again')









