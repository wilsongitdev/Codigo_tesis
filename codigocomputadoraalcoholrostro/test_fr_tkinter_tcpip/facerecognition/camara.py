
import face_recognition
from sklearn import svm
from sklearn.metrics import accuracy_score
import os
import pickle
import cv2
from time import time
####añadida recientemente
import dlib
import face_recognition_models
import numpy as np
# some time later...
font = cv2.FONT_HERSHEY_SIMPLEX 
color=(255,255,255)
grosor=2
# load the model from disk
filename = 'clasificador1.sav' #clasificador 1 o clasificador id
svm = pickle.load(open(filename, 'rb'))

imagen=cv2.imread('imgppt.jpg')
facelocations= face_recognition.face_locations(imagen)
(top,right,bottom,left) = facelocations[0]
# Predict all the faces in the test_fr_tkinter_tcpip image using the trained classifier

test_image_enc = face_recognition.face_encodings(imagen,facelocations,1,'small')[0]
id_ = svm.predict([test_image_enc])
prob=svm.predict_proba([test_image_enc])
nombre=""

print(max(prob[0]))

cv2.rectangle(imagen,(left,top),(right,bottom),color,grosor)
cv2.putText(imagen,id_[0], (left+50,top-90), font, 1, color, grosor, cv2.LINE_AA)
cv2.putText(imagen, str(max(prob[0]))[0:6], (left+50,top-60), font, 1, color, grosor, cv2.LINE_AA)
cv2.imshow('imagen',imagen)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows()

