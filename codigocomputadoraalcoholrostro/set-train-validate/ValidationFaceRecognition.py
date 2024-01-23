import face_recognition
from sklearn import svm
from sklearn.metrics import accuracy_score
import os
import pickle
import cv2

##########################
percentage_image_trained = 70
##############################
# load the model from disk
filename = '../main/clasificador.sav'
svm = pickle.load(open(filename, 'rb'))
# Validation directory
train_dir = os.listdir('../images/train_svm')

face_validation = {}

for person_id in train_dir:
    print("Validando imágenes de:" + str(person_id))
    num_true_rec = 0
    num_false_rec = 0
    num_true_rej = 0
    num_false_rej = 0
    total_images_validated = 0
    iterate_img = 0

    file_list = os.listdir("../images/train_svm/" + person_id)
    file_list.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))  # Ordenar por número en el nombre
    total_image_file = len(file_list)
    total_image_trained = round(0.7 * total_image_file) if total_image_file > 30 else -1 # images suposedly trained

    for person_img in file_list:
        iterate_img += 1

        if iterate_img > total_image_trained:

            # load the test_fr_tkinter_tcpip image with unknown faces into a numpy array
            test_image = face_recognition.load_image_file("../images/train_svm/" + person_id + "/" + person_img)
            # find all the faces in the test_fr_tkinter_tcpip image using the default hog-based model
            face_locations = face_recognition.face_locations(test_image, 1, 'hog')

            if len(face_locations) == 1:
                total_images_validated += 1
                # predict all the faces in the test_fr_tkinter_tcpip image using the trained classifier
                test_image_enc = face_recognition.face_encodings(test_image, face_locations, 1, 'small')[0]
                id_identified_person = svm.predict([test_image_enc])
                prob = max(svm.predict_proba([test_image_enc])[0])

                if prob > 0.90:  # la reconoce
                    if person_id == id_identified_person:  # está en la base de datos
                        num_true_rec += 1
                    else:  # no está en la base de datos
                        num_false_rec += 1
                else:  # no la reconoce
                    if person_id == id_identified_person:  # está en la base de datos
                        num_false_rej += 1
                    else:  # no está en la base de datos
                        num_true_rej += 1

    print(f"Se ha validado las img de {person_id}")

    face_validation[person_id] = {"total_images_validated": total_images_validated,
                                  "num_true_rec": num_true_rec,
                                  "num_true_rej": num_true_rej,
                                  "num_false_rec": num_false_rec,
                                  "num_false_rej": num_false_rej}
print(face_validation)

for key, value in face_validation.items():
    print(f"Datos de: {key}")
    for key1, value1 in value.items():
        print(f"{key1}: {value1}")
# {'00000001': {'num_true_rec': 53, 'num_false_rec': 0, 'num_true_rej': 0, 'num_false_rej': 5, 'total_images': 58},
# '00000002': {'num_true_rec': 0, 'num_false_rec': 0, 'num_true_rej': 0, 'num_false_rej': 0, 'total_images': 0},
# '00000003': {'num_true_rec': 61, 'num_false_rec': 0, 'num_true_rej': 0, 'num_false_rej': 11, 'total_images': 72},
# '00000004': {'num_true_rec': 83, 'num_false_rec': 0, 'num_true_rej': 0, 'num_false_rej': 6, 'total_images': 89},
# '00000005': {'num_true_rec': 113, 'num_false_rec': 0, 'num_true_rej': 0, 'num_false_rej': 7, 'total_images': 120},
# '00000006': {'num_true_rec': 90, 'num_false_rec': 0, 'num_true_rej': 0, 'num_false_rej': 0, 'total_images': 90},
# '00000007': {'num_true_rec': 90, 'num_false_rec': 0, 'num_true_rej': 0, 'num_false_rej': 0, 'total_images': 90},
# '00000008': {'num_true_rec': 0, 'num_false_rec': 0, 'num_true_rej': 11, 'num_false_rej': 0, 'total_images': 11},
# '00000009': {'num_true_rec': 0, 'num_false_rec': 0, 'num_true_rej': 11, 'num_false_rej': 0, 'total_images': 11},
# '00000010': {'num_true_rec': 0, 'num_false_rec': 0, 'num_true_rej': 9, 'num_false_rej': 0, 'total_images': 9}}
