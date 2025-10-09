import tkinter as tk
from tkinter import ttk
 
window = tk.Tk()
window.title('Tkinter Tk_text Widget')
window.geometry('400x400')
 
# This is our TK Text widget
myCombobox = tk.Text(master = window, undo=False, maxundo=150, spacing1=15, spacing2=3, spacing3=5, height=5, wrap='none')
 
# Pack elements ready to push onto form/window
myCombobox.pack()
# run the program to generate window with all packed elements for user interaction
window.mainloop()