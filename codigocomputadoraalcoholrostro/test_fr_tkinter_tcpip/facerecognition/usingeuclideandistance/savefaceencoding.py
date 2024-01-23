import face_recognition
from sklearn import svm
import os
import pickle
import numpy as np

# Training the SVC classifier

# The training data would be all the face encodings from all the known images and the labels are their names
encodings = []
y_etiquetas = []
# Training directory
train_dir = os.listdir('/TESIS/PROYECTO-ELECTRÓNICO/codigocomputadoraalcoholrostro/images/euclidean_distance')
print(train_dir)
# Loop through each person in the training directory
cont_img_train = 0
for person in train_dir:
    pix = os.listdir("/TESIS/PROYECTO-ELECTRÓNICO/codigocomputadoraalcoholrostro/images/euclidean_distance/" + person)

    # Loop through each training image for the current person
    for person_img in pix:
        # Creando las etiquetas
        print(person_img)
        # Get the face encodings for the face in each image file
        face = face_recognition.load_image_file(
            "/TESIS/PROYECTO-ELECTRÓNICO/codigocomputadoraalcoholrostro/images/euclidean_distance/" + person + "/" + person_img)
        face_bounding_boxes = face_recognition.face_locations(face)

        # If training image contains exactly one face
        if len(face_bounding_boxes) == 1:
            face_enc = face_recognition.face_encodings(face, face_bounding_boxes, 1, 'small')[0]
            encodings.append(face_enc)
            y_etiquetas.append(person)

        else:
            print(person + "/" + person_img + " was skipped and can't be used for training")

file1 = open("encodingfaces.txt", "wb")
pickle.dump([encodings, y_etiquetas], file1)
file1.close


# save the model to disk
# filename = '../main/face_encodings.sav'  # clasificador id o clasificador id1
# pickle.dump(clf, open(filename, 'wb'))
