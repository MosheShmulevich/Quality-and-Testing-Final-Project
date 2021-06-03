from tkinter import *


class App(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title("BMI")

        self.lebel = Label(self.root, text ="please enter weight in KG").pack()
        self.weight = StringVar()
        Entry(self.root, textvariable=self.weight).pack()

        self.lebel = Label(self.root, text="please enter height in meter").pack()
        self.height = StringVar()
        Entry(self.root, textvariable=self.height).pack()


        self.buttontext = StringVar()
        Button(self.root, textvariable=self.buttontext, command=self.calculete).pack()
        self.buttontext.set("calculate")

        self.bmi_num = StringVar()
        Label(self.root, textvariable=self.bmi_num).pack()

        self.bmi_text = StringVar()
        Label(self.root, textvariable=self.bmi_text).pack()

        self.root.mainloop()

    def calculete(self):

        weight = float(self.weight.get())
        height = float(self.height.get())
        bmi = float((weight)/(height**2))

        self.bmi_num.set("your BMI is %.2f" % bmi)
        if bmi < 18.5:
           self.bmi_text.set("you are Underweight")
        if 18.5 < BMI <= 25:
            self.bmi_text.set("you are Normal")
        if 25 < bmi<= 29:
            self.bmi_text.set("you are overweight")
        if 30 <= bmi < 40:
            self.bmi_text.set("you are  obesity")
        if bmi > 40:
            self.bmi_text.set("you are  Acute obesity")



App()


def save_info():
    fever_info = fever.get()
    smoking_info = smoking.get()
    pregnant_info = pregnant.get()
    diarrhea_vomiting_info = diarrhea_vomiting.get()
    using_additional_medications_info = using_additional_medications.get()
    background_diseases_info = background_diseases.get()
    BMI_info = BMI.get()

    print(fever_info, smoking_info, pregnant_info, diarrhea_vomiting, using_additional_medications, background_diseases, BMI )

    file = open("p.txt", "w")

    file.write("Do you have a fever? " + str(fever_info))

    file.write("\n")

    file.write("Do you smoke?" + str(smoking_info))

    file.write("\n")

    file.write("Are you pregnant?" + str(pregnant_info))

    file.write("\n")

    file.write("Do you have diarrhea and vomiting?" + str(diarrhea_vomiting_info))

    file.write("\n")

    file.write("Are you taking additional medications?" + str(using_additional_medications_info))

    file.write("\n")

    file.write("Are there any other diseases?" + str(background_diseases_info))

    file.write("\n")

    file.write("your BMI is:" + str(BMI_info))

    file.write("\n")

    file.close()


app = Tk()

app.geometry("700x700")

app.title("Diagnosis of the patient")

heading = Label(text="Python File Handling in Forms", fg="black", bg="blue", width="500", height="3", font="10")

heading.pack()

fever_text = Label(text="Do you have a fever? ")
smoking_text = Label(text="Do you smoke? ")
pregnant_text = Label(text="Are you pregnant? ")
diarrhea_vomiting_text = Label(text="Do you have diarrhea and vomiting? ")
using_additional_medications_text = Label(text="Are you taking additional medications? ")
background_diseases_text = Label(text="Are there any other diseases? ")
BMI_text = Label(text="your BMI: ")


fever_text.place(x=15, y=70)
smoking_text.place(x=15, y=140)
pregnant_text.place(x=15, y=210)
diarrhea_vomiting_text.place(x=15, y=280)
using_additional_medications_text.place(x=15, y=350)
background_diseases_text.place(x=15, y=420)
BMI_text.place(x=15, y=490)


fever = StringVar()
smoking = StringVar()
pregnant = StringVar()
diarrhea_vomiting = StringVar()
using_additional_medications = StringVar()
background_diseases = StringVar()
BMI = StringVar()


fever_entry = Entry(textvariable=fever, width="30")
smoking_entry = Entry(textvariable=smoking, width="30")
pregnant_entry = Entry(textvariable=pregnant, width="30")
diarrhea_vomiting_entry = Entry(textvariable=diarrhea_vomiting, width="30")
using_additional_medications_entry = Entry(textvariable=using_additional_medications, width="30")
background_diseases_entry = Entry(textvariable=background_diseases, width="30")
BMI_entry = Entry(textvariable=BMI, width="30")


fever_entry.place(x=15, y=100)
smoking_entry.place(x=15, y=170)
pregnant_entry.place(x=15, y=240)
diarrhea_vomiting_entry.place(x=15, y=310)
using_additional_medications_entry.place(x=15, y=380)
background_diseases_entry.place(x=15, y=450)
BMI_entry.place(x=15, y=520)



button = Button(app, text="Submit Data", command=save_info, width="30", height="2", bg="grey")

button.place(x=15, y=700)

mainloop()





