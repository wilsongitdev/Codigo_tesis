import face_recognition
import pickle
import cv2
from time import time

# load the model from disk
filename = '../../main/clasificador.sav'  # clasificador 1 o clasificador id
svm = pickle.load(open(filename, 'rb'))


font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 255, 255)
grosor = 3

image_path = "imgppt.jpg"
image = cv2.imread(image_path)
# Load the test_fr_tkinter_tcpip image with unknown faces into a numpy array
# test_image = face_recognition.load_image_file('images/wilsonvolteado.jpg')
start_time = time()
# Find all the faces in the test_fr_tkinter_tcpip image using the default HOG-based model
facelocations = face_recognition.face_locations(image, 1, 'hog')
if len(facelocations) == 1:
    (top, right, bottom, left) = facelocations[0]
    # Predict all the faces in the test_fr_tkinter_tcpip image using the trained classifier

    test_image_enc = face_recognition.face_encodings(image, facelocations, 1, 'small')[0]
    print(test_image_enc)
    id_ = svm.predict([test_image_enc])
    prob = svm.predict_proba([test_image_enc])
    nombre = ""
    if (id_[0] == '44687542'):
        nombre = "Jackie"
    if (id_[0] == '47488888'):
        nombre = "Sara"
    if (id_[0] == '00000005'):
        nombre = "Wilson"
    if (id_[0] == '75123454'):
        nombre = "Luis"

    cv2.rectangle(image, (left, top), (right, bottom), color, grosor)
    cv2.putText(image, nombre, (left + 50, top - 50), font, 1.2, color, grosor, cv2.LINE_AA)
    cv2.putText(image, str(max(prob[0]) * 100)[0:6], (left + 50, top - 15), font, 1.2, color, grosor, cv2.LINE_AA)
    cv2.imshow('Imagen', image)
    cv2.imwrite('img_rec_user.png',image)
    cv2.waitKey(0)
    elapsed_time = time() - start_time
    print("Elapsed time: %0.10f seconds." % elapsed_time)

else:
    print("No se ha detectado rostro")

