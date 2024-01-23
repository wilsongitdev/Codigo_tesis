import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from windows import improveimagequality
import cv2
import time

improveimagequality()
root = tk.Tk()
root.geometry("800x400")
root.resizable(False, False)
root.title("Imagen")
# print(font.families())
fontcreated = font.Font(family="Roman", size=15, weight="bold")


def hellosmoke():
    print("Hola humo")

    image1 = Image.open("../../images/test/Smash.jpg").resize(size=(200, 200))
    photo1 = ImageTk.PhotoImage(image1)
    labelimg.config(image=photo1)
    labelimg.image = photo1


image = Image.open("../../images/test/EliteWolves.jpg").resize(size=(200, 200))
photo = ImageTk.PhotoImage(image)

labelimg = ttk.Label(root, text="Rostro", image=photo, compound="bottom", font=fontcreated)
# for children in root.winfo_children():
#     children.grid_configure(padx=10, pady=10)
# labelimg.config()
labelimg.pack()
label = ttk.Label(text="Hi", font=fontcreated)
# label.config()
label.pack()

btnStyle = ttk.Style()
btnStyle.configure("W.TButton",font=fontcreated)
buttonNewMedition = ttk.Button(root, text="Nueva medición", command=hellosmoke, style="W.TButton")
buttonNewMedition.pack()


root.mainloop()
