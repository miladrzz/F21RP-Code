import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

f = open("./temp-data.json")
data = json.load(f)

def search():
    global details
    global data
    global d1
    global d2
    global d3
    global d4
    global d5
    d1 = data1txt.get()
    try:
        d2 = int(data2txt.get())
    except ValueError:
        err = Label(root,text="That is not a number!")
        err.pack()
    d3 = data3txt.get()
    d4 = data4txt.get()
    d5 = data5txt.get()
    details = [d1,d2,d3,d4,d5]
    for item in data["data"]:
        age = item["age"]
        diff = max(age,int(details[1]))-min(age,int(details[1]))
        if diff<=3:
            game = item["game"]
            if game == details[2]:
                pro = item["level"]
                if pro == details[3]:
                    answer = "\nMatch Found! Here are your new companion's details:\n"
                    answer= answer + "Name: "+item["name"] +"\n"
                    answer = answer + "Age: "+str(item["age"])+"\n"
                    answer= answer+"Plays: "+item["game"]+"\n"
                    answer+"Level of proficiency: "+item["level"]+"\n"

                    result_lable= Label(root, text=answer)
                    result_lable.pack()

details = []
root = Tk()

root.title('GameMate')

label_age = Label(root, text="Name")
label_age.pack()
data1txt = Entry(root,width=25)
data1txt.pack()

label_age = Label(root, text="Age")
label_age.pack()
data2txt = Entry(root,width=25)
data2txt.pack()

label_age = Label(root, text="Game")
label_age.pack()
data3txt = Entry(root,width=25)
data3txt.pack()

label_age = Label(root, text="Proficiency")
label_age.pack()
data4txt = Entry(root,width=25)
data4txt.pack()

label_age = Label(root, text="Platform")
label_age.pack()
data5txt = Entry(root,width=25)
data5txt.pack()

d1 = None
d2 = None
d3 = None
d4 = None
d5 = None

button_frame = Frame(root)
button_frame.pack()

search_btn = Button(button_frame,text="Search",command=search)
search_btn.pack()
root.mainloop()