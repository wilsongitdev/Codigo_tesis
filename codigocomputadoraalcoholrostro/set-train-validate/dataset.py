"""
este codigo registra la info del usuario,

si NO esta registrado, HACE LO SIGUIENTE:
- que se rellene sus datos, tome una foto(presionar la tecla "Q")
-REGISTRA EN LA BASE DE DATOS LA FOTO
- CREA EL SET DE DATOS PARA  entrenamiento del algoritmo de reconocimiento de
rostro.


Si el usuario esta registrado
PREGUNTA SI DESEAS VOLVER A CREAR SET DE DATOS PARA EL ENTRENAMIENTO?

"""

import cv2
import os
import requests


def user_create_dataset(form_data_user):
    print("Creando set de datos")
    for count in range(NUMBER_PICTURES):
        _, image = web_cam.read()
        cv2.imshow("Creating dataset", image)
        cv2.imwrite("../images/train_svm/" + form_data_user["dni"] + "/" +
                    form_data_user["name"] + "_" + str(count) + ".jpg", image)
        cv2.waitKey(60)

    web_cam.release()
    cv2.destroyAllWindows()


def send_user_data_to_database(form_data_user):

    while True:
        _, image = web_cam.read()
        cv2.imshow("Camera", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            _, img_encoded = cv2.imencode('.jpg', image)

            response = requests.post(URL_INSERT_USER, data=form_data_user,
                                     files={"user_image": ("example.jpg", img_encoded, "image/jpeg")})
            js_response = response.json()
            cv2.destroyAllWindows()
            if js_response['status'] == 1:
                user_create_dataset(form_data_user) # CREA EL SET DE DATOS PARA EL ENTRENAMIENTO DEL ALGORITMO
                print("Se ha registrado sus datos correctamente")
            else:
                print("No se puede realizar el entrenamiento")
                print(js_response['description'])
            break


def data_register():
    name = input("Ingrese su nombre: ")
    lastname = input("Ingrese su apellido: ")
    email = input("Ingrese su correo: ")
    phone_number = input("Ingrese su celular: ")
    city = input("Ingrese su ciudad: ")
    country = input("Ingrese su país: ")
    return {"dni": dni, "email": email, "name": name, "lastname": lastname,
            "phone_number": phone_number, "city": city, "country": country}


NUMBER_PICTURES = 300
URL_LIST_USER = "https://proyectoalcohol.000webhostapp.com/proy_control_alc/user/listuser.php"
URL_INSERT_USER = "https://proyectoalcohol.000webhostapp.com/proy_control_alc/user/insertuser.php"

web_cam = cv2.VideoCapture(0)
# cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('Camera', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
print("Bienvenido")
dni = input("Ingrese su DNI: ")

js_response_list_user = requests.post(URL_LIST_USER, data={"numberpage": 1, "sizelist": 50}).json()
list_user = js_response_list_user["objModel"]["elements"]

is_user = False # FALSE, NO EXISTE EN LA BD, TRUE LO CONTRARIO
# existe en directorio?
if not os.path.exists("../images/train_svm/" + dni):
    #CREA EL DIRECCTORIO PARA UN NUEVO USUARIO
    os.makedirs("../images/train_svm/" + dni)
#existe en la bd?
for user in list_user:
    if user["DNI"] == dni:
        is_user = True

if not is_user: # no esta registrado
    print("Usuario no registrado")
    data_to_send = data_register()
    send_user_data_to_database(form_data_user=data_to_send) #se abre camara y se debe persionar q para toma de foto
else: # esta registrado
    for user in list_user:
        if user["DNI"] == dni:
            print("Usuario registrado")
            override_answer = input(
                f"Quieres sobreescribir las imágenes para la persona con DNI: {dni} (Y/N)?: ".upper())
            if override_answer == "Y": # sobreescribir imagenes
                data_to_send = data_register()
                user_create_dataset(data_to_send)
                print("Se han obtenido las imágenes")
            else: # no sobreescribir imágenes
                print("No se sobreescribieron las imágenes")

#########################
