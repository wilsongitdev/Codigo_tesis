import face_recognition
import pickle
import cv2
from time import time

# load the model from disk
filename = '../../main/clasificador.sav'  # clasificador 1 o clasificador id
svm = pickle.load(open(filename, 'rb'))

webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 480)
font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 255, 255)
grosor = 2
while (True):
    # Cargar img de la camara web
    ret, test_image = webcam.read()
    # Load the test_fr_tkinter_tcpip image with unknown faces into a numpy array
    # test_image = face_recognition.load_image_file('images/wilsonvolteado.jpg')
    start_time = time()
    # Find all the faces in the test_fr_tkinter_tcpip image using the default HOG-based model
    facelocations = face_recognition.face_locations(test_image, 1, 'hog')
    if len(facelocations) == 1:
        (top, right, bottom, left) = facelocations[0]
        # Predict all the faces in the test_fr_tkinter_tcpip image using the trained classifier

        test_image_enc = face_recognition.face_encodings(test_image, facelocations, 1, 'small')[0]
        print(test_image_enc)
        print(max(test_image_enc))
        id_ = svm.predict([test_image_enc])
        prob = svm.predict_proba([test_image_enc])
        nombre = ""
        if (id_[0] == '44687542'):
            nombre = "Jackie"
        if (id_[0] == '47488888'):
            nombre = "Sara"
        if (id_[0] == '74881892'):
            nombre = "Wilson"
        if (id_[0] == '75123454'):
            nombre = "Luis"
        print(nombre)
        cv2.rectangle(test_image, (left, top), (right, bottom), color, grosor)
        cv2.putText(test_image, nombre, (left + 50, top - 90), font, 1, color, grosor, cv2.LINE_AA)
        cv2.putText(test_image, str(max(prob[0]))[0:6], (left + 50, top - 60), font, 1, color, grosor, cv2.LINE_AA)
        cv2.imshow('Imagen', test_image)

        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("No se ha detectado rostro")

webcam.release()
cv2.destroyAllWindows()
