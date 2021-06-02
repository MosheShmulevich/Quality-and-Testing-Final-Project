from tkinter import *


def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    origin_info = origin.get()
    gender_info = gender.get()

    print(firstname_info, lastname_info, age_info, origin_info, gender_info)

    file = open("PatientsInfo.txt", "w")

    file.write("Your First Name is: " + firstname_info)

    file.write("\n")

    file.write("Your Last Name is: " + lastname_info)

    file.write("\n")

    file.write("Your Age is: " + str(age_info))

    file.write("\n")

    file.write("Your Origin is: " + origin_info)

    file.write("\n")

    file.write("Your Gender is: " + gender_info)

    file.write("\n")

    file.close()


app = Tk()

app.geometry("350x700")

app.title("Save Data to a text file")

heading = Label(text="Python File Handling in Forms", fg="black", bg="lightblue", width="500", height="3", font="10")

heading.pack()

firstname_text = Label(text="FirstName :")
lastname_text = Label(text="LastName :")
age_text = Label(text="Age :")
origin_text = Label(text="Origin :")
gender_text = Label(text="Gender :")

firstname_text.place(x=15, y=70)
lastname_text.place(x=15, y=140)
age_text.place(x=15, y=210)
origin_text.place(x=15, y=280)
gender_text.place(x=15, y=350)

firstname = StringVar()
lastname = StringVar()
age = IntVar()
origin = StringVar()
gender = StringVar()

first_name_entry = Entry(textvariable=firstname, width="30")
last_name_entry = Entry(textvariable=lastname, width="30")
age_entry = Entry(textvariable=age, width="30")
origin_entry = Entry(textvariable=origin, width="30")
gender_entry = Entry(textvariable=gender, width="30")

first_name_entry.place(x=15, y=100)
last_name_entry.place(x=15, y=170)
age_entry.place(x=15, y=240)
origin_entry.place(x=15, y=310)
gender_entry.place(x=15, y=380)

button = Button(app, text="Submit Data", command=save_info, width="30", height="2", bg="blue")

button.place(x=15, y=500)

mainloop()
""""
root.title('Patients Information')

label1 = Label(root, text="Name")
label2 = Label(root, text="Family")
label3 = Label(root, text="Age")
label4 = Label(root, text="Origin")
label5 = Label(root, text="Gender")
label6 = Label(root, text="Condition")

label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)
label4.grid(row=3)
label5.grid(row=4)
label6.grid(row=5)

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=5, column=1)


EntryButton = Button(root, text="Enter",).grid(row=6, column=0)

root.mainloop() """
