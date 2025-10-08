import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tkinter Radiobutton Widget')
window.geometry('400x400')

# Frame
radiobutton_frame = tk.Frame(window)

# This is our Radiobuttons
int_var = tk.IntVar()
Int_radiobutton_1 = ttk.Radiobutton(radiobutton_frame, value = 1, variable = int_var, text = 'This is One')
Int_radiobutton_2 = ttk.Radiobutton(radiobutton_frame, value = 2, variable = int_var, text = 'This is Two')

# display which button is pressed
output_label = tk.Label(window, text = "")

# Function to confirm which button was pressed
def confirm_selection():
    if int_var.get() == 1:
        output_label.config(text = "You selected: This is One")
    elif int_var.get() == 2:
        output_label.config(text = "You selected: This is Two")
    else:
        output_label.config(text = "No option selected")

# Add the command
Int_radiobutton_1.config(command = confirm_selection)
Int_radiobutton_2.config(command = confirm_selection)

# Pack elements 
radiobutton_frame.pack()
Int_radiobutton_1.pack()
Int_radiobutton_2.pack()
output_label.pack()

# run 
window.mainloop()