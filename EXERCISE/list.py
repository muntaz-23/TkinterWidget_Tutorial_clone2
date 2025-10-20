import tkinter as tk
from tkinter import ttk

#window
window = tk
window.title = 'List'
window.geometry = ("400x400")
root = tk.Tk()

subjects = ["English", "Science", "Computing" ,"Arabic", "Social Studies", "Sports Science"]


variable_bool = True
variable_int = 7
subjects.append(variable_bool)
subjects.append(variable_int)

subjects.extend(["French", "Geography"])
print(subjects[9])
print(subjects[10])


print(subjects[7])
print(subjects[8])
print(len(subjects))

#Spinbox
int_var = tk.IntVar()
Number_spinbox = tk.Spinbox(root, from_= 0, to=100, increment=.01, textvariable = int_var, font = 'Calibri 24 bold')
Number_spinbox.pack()



