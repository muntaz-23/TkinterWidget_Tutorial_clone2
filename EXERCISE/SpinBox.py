import tkinter as tk
from tkinter import ttk

#This section creates the tkinter Window and adds the required elements to it
window = tk.Tk()
window.title('Tkinter Spinbox Widget')
window.geometry('400x400')

#Spinbox
int_var = tk.IntVar()
Number_spinbox = ttk.Spinbox(window, from_=0, to=100, increment=.01, textvariable = int_var, font = 'Calibri 24 bold')

subject_list = ['Maths', 'English', 'Science', 'Computing', 'Latin', 'Arabic', 'Social Studies']
string_var = tk.StringVar()
Subject_spinbox = ttk.Spinbox(textvariable = string_var, font = 'Calibri 24 bold', values = subject_list)

#Pack elements in frames ready to push onto form/window
Number_spinbox.pack()
Subject_spinbox.pack()

#run
window.mainloop()
