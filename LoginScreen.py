from tkinter import *
from functools import partial

def validateLogin(username, password, id):
    print("username entered :", username.get())
    print("password entered :", password.get())
    print("id entered :", id.get())


#window
tkWindow = Tk()
tkWindow.geometry('280x120')
tkWindow.title('Login Screen')

#username label and text entry box (must include 6-8 characters , maximum 2 digits)
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box (must include 8-10 characters, atleast 1 letter, 1 digit, 1 special character{!,@,#,$,%,^,&,*,(,),-,+,=}
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

#id label and id entry box (must be 9 digits between 0 to 9)
idLabel = Label(tkWindow, text="ID").grid(row=2, column=0)
id = StringVar()
idEntry = Entry(tkWindow, textvariable=id).grid(row=2, column=1)

validateLogin = partial(validateLogin, username, password, id)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()