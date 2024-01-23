from project_modules import *
import requests
import time
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import numpy as np
from windows import improveimagequality



        
def buttonpressed():
        gpio_rgb_stop_and_clean()
        led_start()
        led_rgb(100, 100, 100)
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

        usermessage.set("Exhale")
        label_main_message.update()

        image_webcam_rgb = detectairflow()
        
        usermessage.set("Exhalación detectada")
        
        label_main_message.update()
        
        matr, vprom = ads1115_get_vprom()
        print(f"Voltaje promedio: {vprom} V de {len(matr)} muestras")

        alcohol, alcbac = get_alcohol_level_mgL_BAC(vprom, tara)
        id_person, person_rgb, face_detection = get_image_of_recognized_person(image_webcam_rgb, alcohol, alcbac)
        
        #final_message = f"Nivel alcohólico {alcohol} mg/L - {alcbac} BAC" if face_detection is True else "No se ha detectado rostro"
        #usermessage.set(final_message)
        if face_detection :# se detecto rostro
                
                url = 'https://proyectoalcohol.000webhostapp.com/proy_control_alc/user/Insertalcoholdata.php'

                # Convert the image to bytes using OpenCV's imencode() method
                _, img_encoded = cv2.imencode('.jpg', person_rgb)


                form_data = {
                    'ing_alcohol': "1" if args[0] is True else "0",
                    'alc_mgl': f'{alcohol}',
                    'alc_bac': f'{alcbac}',
                    'dni': f'{id_person}'
                }

                files = {
                    "img": ("image.jpg", img_encoded, "image/jpeg")
                }

                # Send the image data using requests.post() method
                """
                response = requests.post(url, data=form_data, files=files)
                output = response.text
                print('The response from the server is: \n', output)
                """
                if float(alcohol) or float(alcbac) > 0:
                    print("se detectó alcohol")
                    led_rgb(100, 0, 0)
                else:
                    led_rgb(0, 100, 0)
                print(alcohol)
                usermessage.set(f"Nivel alcohólico {alcohol:.3f} mg/L - {alcbac:.3f} BAC")
        
        else:# no se detecto rostro
                usermessage.set("No se ha detectado rostro")
        
        person_brg = cv2.cvtColor(person_rgb, cv2.COLOR_RGB2BGR)
        person_brg_resized = cv2.resize(person_brg, (640, 480), interpolation = cv2.INTER_AREA)
        screen_image = ImageTk.PhotoImage(Image.fromarray(person_brg_resized))
        label_image.config(image=screen_image, text="")
        label_image.image = screen_image
        label_image.pack(expand=True, fill="both", pady=30)
        label_image.update()
        time.sleep(6)
        label_image.pack_forget()
        label_main_message.pack_forget()
        button_new_measure.pack(expand=True, pady=240, padx=240, fill="both")
        led_rgb(0, 0, 0)
        gpio_rgb_stop_and_clean()


        


improveimagequality()
root = tk.Tk()
usermessage = tk.StringVar(value="Has ingerido alcohol")
root.geometry("800x400")
root.title("Proyecto")
root.attributes('-fullscreen', True)
root.configure(pady=50, padx=60, background="orange")
fontcreated = font.Font(size=36, weight="bold")
btnStyle = ttk.Style()
btnStyle.configure("W.TButton", font=fontcreated)

button_new_measure = ttk.Button(root, command=buttonpressed, text="Nueva Medición", style="W.TButton")
button_new_measure.pack(expand=True, pady=240, padx=240, fill="both")

label_main_message = ttk.Label(root, textvariable=usermessage, font=fontcreated, anchor="center")
label_main_message.pack_forget()

button_yes = ttk.Button(root, command=lambda: buttonanswer(True), text="Sí", style="W.TButton")
button_yes.pack_forget()

button_no = ttk.Button(root, command=lambda: buttonanswer(False), text="No", style="W.TButton")
button_no.pack_forget()

label_image = ttk.Label(root, image="", text="", compound="bottom", font=fontcreated, anchor="center")
label_image.pack_forget()
root.mainloop()
        

        


