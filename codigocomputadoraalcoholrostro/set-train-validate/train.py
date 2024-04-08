# Train multiple images per person
# Find and recognize faces in an image using a SVC with scikit-learn

"""
Structure:
        <test_image>.jpg
        <train_dir>/
            <person_1>/
                <person_1_face-1>.jpg
                <person_1_face-2>.jpg
                .
                .
                <person_1_face-n>.jpg
           <person_2>/
                <person_2_face-1>.jpg
                <person_2_face-2>.jpg
                .
                .
                <person_2_face-n>.jpg
            .
            .
            <person_n>/
                <person_n_face-1>.jpg
                <person_n_face-2>.jpg
                .
                .
                <person_n_face-n>.jpg
"""

import face_recognition
from sklearn import svm
import os
import pickle
import numpy as np

##########################
PERCENTAGE_FOR_TRAINING = 70
##############################
# Training the SVC classifier

# The training data would be all the face encodings from all the known images and the labels are their names
encodings = []
labels = []
# Training directory
train_dir = os.listdir('../images/train_svm/')

face_training = {}
# Loop through each person in the training directory
print(train_dir)

for person_id in train_dir:

    print(f"Storing images from {person_id}")

    file_list = os.listdir("../images/train_svm/" + person_id)
    file_list.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))  # Ordenar por número en el nombre
    total_images_train = round((PERCENTAGE_FOR_TRAINING / 100) * len(file_list))
    iterate_img = 0
    total_images_trained = 0
    # Loop through each training image for the current person
    print(file_list)
    for person_img in file_list:
        iterate_img += 1

        if iterate_img < total_images_train:
            # Get the face encodings for the face in each image file
            face = face_recognition.load_image_file("../images/train_svm/" + person_id + "/" + person_img)
            face_bounding_boxes = face_recognition.face_locations(face)
            # If training image contains exactly one face
            if len(face_bounding_boxes) == 1:
                total_images_trained += 1
                #print(f"person_img: {person_img}, total_images_trained: {total_images_trained}")
                face_enc = face_recognition.face_encodings(face, face_bounding_boxes, 1, 'small')[0]
                # Add face encoding for current image with corresponding label (name) to the training data
                encodings.append(face_enc)
                labels.append(person_id)

            else:
                print(person_id + "/" + person_img + " was skipped and can't be used for training")
    face_training[person_id] = {"total_images_trained": total_images_trained}
    print(face_training)
# Create and train the SVC classifier
clf = svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=True, tol=0.001,
              cache_size=200,
              class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False,
              random_state=None)
clf.fit(encodings, np.array(labels))

# save the model to disk
filename = '../main/clasificador.sav'  # clasificador id o clasificador id1
pickle.dump(clf, open(filename, 'wb'))
