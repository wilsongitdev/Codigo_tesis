import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# from windows import improveimagequality
import cv2
import time


# improveimagequality()
root = tk.Tk()
root.geometry("800x400")
root.resizable(False,False)
root.title("Imagen")

Wait = tk.StringVar()
web_cam = cv2.VideoCapture(0)
_, imagen_marco = web_cam.read()
def hellosmoke():
    print("Hola humo")
    _, imagen_marco = web_cam.read()
    cv2_im = cv2.cvtColor(imagen_marco, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im)
    image1 = pil_im.resize(size=(200, 200))
    photo1 = ImageTk.PhotoImage(image1)
    labelimg.config(image=photo1)
    labelimg.image = photo1

image = Image.open("../images/test/EliteWolves.jpg").resize(size=(200, 200))
photo = ImageTk.PhotoImage(image)

labelimg = ttk.Label(root, text="Rostro", image=photo, padding=10, compound="bottom", font=("GiGi",20))
# labelimg.config()
labelimg.pack()

label = ttk.Label(padding=10, text="Hi", font=("GiGi",10))
# label.config()
label.pack()

buttonNewMedition = ttk.Button(root, text="Nueva medición", command=hellosmoke)
buttonNewMedition.pack()
root.mainloop()
