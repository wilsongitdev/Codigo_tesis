import face_recognition
import cv2
import os
import numpy as np
from imutils import paths
from PIL import Image
import time



image0=face_recognition.load_image_file("../../images/test/obama_and_biden.jpg")
#image=cv2.imread('images/kit_with_rose.jpg')
image=cv2.cvtColor(image0,cv2.COLOR_BGR2RGB)
face_locations = face_recognition.face_locations(image)
face_encoding=face_recognition.face_encodings(image0)[0]
print(face_encoding)


	
