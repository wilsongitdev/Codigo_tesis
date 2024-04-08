import os
import socket
import pickle
import cv2
import face_recognition
import requests


def send_confirmation(conn, faces=[], id_person=None, prob=0, name=None):
    response = {
        "id": id_person,
        "name": name,
        "prob": prob,
        "face_locations": faces
    }
    confirmation_data = pickle.dumps(response)
    conn.sendall(confirmation_data)


def search_and_find_file(base_directory, directory_name):
    # Full path of the directory to search
    directory_path = os.path.normpath(os.path.join(base_directory, directory_name))
    # Check if the directory exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Get the list of files in the directory
        files_in_directory = os.listdir(directory_path)
        first_file = files_in_directory[0]
        ## splitea en nombre y extension y luego se obtiene el nombre
        first_file_without_extension = os.path.splitext(first_file)[0][0:-2]
        return first_file_without_extension
    else:
        return None


def function_face_recognition(image, svm):
    # reconocimiento de rostro
    faces = face_recognition.face_locations(image, number_of_times_to_upsample=1, model="hog")
    id_person = ""
    prob = 0
    if len(faces) >= 1:
        # preprocesamiento por si las moscas
        ######## aprueba (detectar rostro mas grande de la imagen) ################################################
        max_area = 0
        largest_face_location = None

        for face_location in faces:
            top, right, bottom, left = face_location
            area = (bottom - top) * (right - left)
            if area > max_area:
                max_area = area
                largest_face_location = face_location

        faces_encodings = face_recognition.face_encodings(face_image=image, known_face_locations=largest_face_location,
                                                          model="large")
        #################################################################3
        id_person = svm.predict(faces_encodings)[0]
        prob = max(svm.predict_proba(faces_encodings)[0])
    # Especifica el directorio base y los nombres de directorio y archivo
    base_directory = "../images/train_svm"  # Cambia a tu directorio base
    directory_name = id_person
    name = search_and_find_file(base_directory, directory_name)

    return faces, id_person, name, prob,


def receive_data_pickled_and_load(conn):#NO USADOOO :C
    data_received = b""
    data_size_bytes = conn.recv(4)  # Recibe el tamaño de la imagen en bytes
    data_size = int.from_bytes(data_size_bytes, byteorder='big')

    while len(data_received) < data_size:
        partial_data = conn.recv(4096)
        data_received += partial_data

    # Recibe la imagen desde el cliente
    total_data_received = pickle.loads(data_received)
    return total_data_received


def start_server():
    host = '192.168.1.39'  # Cambia a la dirección IP del servidor si es necesario
    port = 10000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Esperando la conexión en {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Conexión establecida desde {addr}")

    filename = './clasificador.sav'
    svm = pickle.load(open(filename, 'rb'))
    try:
        while True:
            data = b""
            image_size_bytes = conn.recv(4)  # Recibe el tamaño de la imagen en bytes
            image_size = int.from_bytes(image_size_bytes, byteorder='big')

            while len(data) < image_size:
                chunk = conn.recv(4096)
                data += chunk

            # Recibe la imagen desde el cliente
            image_data = pickle.loads(data)
            image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

            faces, id_person, name, prob = function_face_recognition(image, svm)
            # Envía un mensaje de confirmación al cliente
            send_confirmation(conn, faces=faces, id_person=id_person, prob=prob, name=name)

            if len(faces) > 0:
                total_data_received = b""
                total_data_bytes = conn.recv(4)

                total_data_size = int.from_bytes(total_data_bytes, byteorder='big')
                # print(f"total_data_server_size: {total_data_server_size}") # 66335

                while len(total_data_received) < total_data_size:
                    data_received = conn.recv(4096)
                    total_data_received += data_received

                received_data = pickle.loads(total_data_received)
                # Send the image data using requests.post() method
                url = 'https://proyectoalcohol.000webhostapp.com/proy_control_alc/user/Insertalcoholdata.php'
                form_data = received_data['form_data']
                files = received_data['files']
                """
                response = requests.post(url, data=form_data, files=files)
                output = response.text
                print('The response from the server is: \n', output)
                """
    except (OSError, IndexError) as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    start_server()
