from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Doctors Application')

#a function that shows a warning message if 1 or more of the fields is incorrect (username, password, id)
def Popup():
    messagebox.showwarning("Error Message", "Wrong username, password or ID.\nPlease try again.")



Button(root, text="Login", command=Popup).pack()

root.mainloop()
