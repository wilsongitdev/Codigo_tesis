import time
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from windows import improveimagequality
import cv2


def buttonpressed():
    print("pressed")
    usermessage.set("Haz ingerido alcohol")
    button_new_measure.pack_forget()
    label_main_message.pack(ipady=10, fill="x")
    button_yes.pack(side="left", expand=True)
    button_no.pack(side="left", expand=True)


def buttonanswer(*args):
    # ocultar botones si/no
    button_yes.pack_forget()
    button_no.pack_forget()
    # mostrar mensaje si/no en el mensaje principal
    btn_yes_no = "Sí" if args[0] is True else "No"
    usermessage.set(btn_yes_no)
    label_main_message.update()
    time.sleep(1)

    usermessage.set("Sople")
    label_main_message.update()

    ret, image_webcam_bgr = cap.read()
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)  # permite la config de t_exp
    cap.set(cv2.CAP_PROP_EXPOSURE, 0.03)  # texp entre 0 y 1
    # print(cap.get(cv2.CAP_PROP_EXPOSURE))
    cv2.waitKey(10)

    image_webcam_rgb = cv2.cvtColor(image_webcam_bgr, cv2.COLOR_BGR2RGB)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)  # permite la config de t_exp
    cap.set(cv2.CAP_PROP_EXPOSURE, 0.03)  # texp entre 0 y 1

    usermessage.set("Soplido detectado")
    label_main_message.update()
    time.sleep(2)
    usermessage.set("Nivel alcohólico 0.5mg/L - 0.01BAC")

    image_face = Image.fromarray(image_webcam_rgb)
    photo = ImageTk.PhotoImage(image_face)

    label_image.config(image=photo)
    label_image.image = photo
    label_image.pack(expand=True, fill="both", pady=50)
    label_image.update()
    time.sleep(2)
    label_image.pack_forget()
    label_main_message.pack_forget()
    button_new_measure.pack(expand=True, pady=280, padx=280, fill="both")
    time.sleep(2)


cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 800)

improveimagequality()
root = tk.Tk()
usermessage = tk.StringVar(value="Has ingerido alcohol")
root.geometry("800x400")
root.title("Proyecto")
root.attributes('-fullscreen', True)
root.configure(pady=50, padx=40, background="orange")
fontcreated = font.Font(size=46, weight="bold")
btnStyle = ttk.Style()
btnStyle.configure("W.TButton", font=fontcreated)

button_new_measure = ttk.Button(root, command=buttonpressed, text="Nueva Medición", style="W.TButton")
button_new_measure.pack(expand=True, pady=280, padx=280, fill="both")

label_main_message = ttk.Label(root, textvariable=usermessage, font=fontcreated, anchor="center", background="green")
label_main_message.pack_forget()

button_yes = ttk.Button(root, command=lambda: buttonanswer(True), text="Sí", style="W.TButton")
button_yes.pack_forget()

button_no = ttk.Button(root, command=lambda: buttonanswer(False), text="No", style="W.TButton")
button_no.pack_forget()

label_image = ttk.Label(root, compound="bottom", anchor="center", background="blue")
label_image.pack_forget()
root.mainloop()
