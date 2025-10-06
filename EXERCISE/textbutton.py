import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Tkinter Checkbutton Widget')
window.geometry('400x400')

# This is our Checkbutton
bool_var = tk.BooleanVar()
Boolean_checkbutton = tk.Checkbutton(window, variable = bool_var, text = "Are you happy?", onvalue = True)

# Pack elements in frames ready to push onto form/window
Boolean_checkbutton.pack()

# Label to display message
label = tk.Label(window, text = "")
label.pack()

# Function to update
def update_label():
    if bool_var.get():
        label.config(text = "I am very HAPPY for you!")
    else:
        label.config(text = "I am sorry, better days ahead!")

# Add the command to Checkbutton
Boolean_checkbutton.config(command = update_label)

# run
window.mainloop()