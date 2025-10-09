import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Tkinter Combobox Widget')
window.geometry('400x400')

# Label 
label = tk.Label(window, text="Select an option from the combobox")
label.pack(pady=10)
 
# Function to update label based on combobox selection
def on_select(event):
    selected_option = string_var.get()
    label.config(text=f"Selected: {selected_option}")
 
# Function to be called before dropdown list is shown
def update_combobox_values():
   myCombobox['values'] = ['This Option', 'That Option', 'Another Option']

#combobox widget
string_var = tk.StringVar()
myCombobox = ttk.Combobox(master = window, textvariable = string_var, values=['This Options', 'That Options', 'Another Option'])
postcommand=update_combobox_values 

#update
myCombobox.bind("ComboboxSelected", on_select)

#pack
myCombobox.pack()

#run
window.mainloop()




