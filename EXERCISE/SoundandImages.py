import tkinter as tk
from winsound import *
from tkinter import PhotoImage

#window
window = tk.Tk()
window.title("Image & Sound in Tkinter")

#Title
title_label = tk.Label(master = window, text = 'Image & Sound', font = 'Calibri 24 bold')
title_label.pack()

#image
image2 = PhotoImage(file="grading_System.png")

#label for image
image_label = tk.Label(window, image=image2)
image_label.pack()

#load iamge
image = PhotoImage(file="play-button.png")

#load a sound
play = lambda: PlaySound("lion_growl.wav", SND_FILENAME)

#BUTTON WIDGET
button = tk.Button(window, image=image, command = play)
button.pack(pady=20)
#loop
window.mainlooop()


