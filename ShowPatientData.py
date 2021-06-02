from tkinter import *
from tkinter import filedialog
window = Tk()
window.title('Medical diagnosis and recommended treatment')
window.geometry("200x200")


def openFile():
    filepath = filedialog.askopenfilename(initialdir="\\Users\\mosheshmulevich\\Desktop\\Quality and Testing Project",
                                          title="Open file", filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()
button = Button(text="Open", command=openFile)
button.pack()


window.mainloop()
