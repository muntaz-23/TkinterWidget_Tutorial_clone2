import tkinter as tk
from tkinter import ttk

#window
window = tk
window.title = 'List'
window.geometry = ("400x400")
root = tk.Tk()

subjects = ["Maths", "English", "Science", "Computing" ,"Arabic", "Social Studies", "Sports Science"]
subjects.pop(2)
subjects.remove("Maths")
print(subjects)

variable_bool = True
variable_int = 7
subjects.append(variable_bool)
subjects.append(variable_int)

print(subjects[6])
print(subjects[6])

print(len(subjects))

subjects.extend(["French", "Geography"])
print(subjects[7])

#Spinbox
int_var = tk.IntVar()
Number_spinbox = tk.Spinbox(root, from_= 0, to=100, increment=.01, textvariable = int_var, font = 'Calibri 24 bold')
Number_spinbox.pack()



