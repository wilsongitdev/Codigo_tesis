import face_recognition
import cv2
import os
import numpy as np
from PIL import Image
import time

def alignFace(image, face_locations, face_landmarks, desiredFaceWidth, desiredFaceHeight):
	
	'''
	Let's find and angle of the face. First calculate 
	the center of left and right eye by using eye landmarks.
	'''
	leftEyePts = face_landmarks[0]['left_eye']
	rightEyePts = face_landmarks[0]['right_eye']

	leftEyeCenter = np.array(leftEyePts).mean(axis=0).astype("int")
	rightEyeCenter = np.array(rightEyePts).mean(axis=0).astype("int")

	leftEyeCenter = (leftEyeCenter[0],leftEyeCenter[1])
	rightEyeCenter = (rightEyeCenter[0],rightEyeCenter[1])

	# draw the circle at centers and line connecting to them
	cv2.circle(image, leftEyeCenter, 2, (255, 0, 0), 10)
	cv2.circle(image, rightEyeCenter, 2, (255, 0, 0), 10)
	cv2.line(image, leftEyeCenter, rightEyeCenter, (255,0,0), 10)

	# find and angle of line by using slop of the line.
	dY = rightEyeCenter[1] - leftEyeCenter[1]
	dX = rightEyeCenter[0] - leftEyeCenter[0]
	angle = np.degrees(np.arctan2(dY, dX))

	# to get the face at the center of the image,
	# set desired left eye location. Right eye location 
	# will be found out by using left eye location.
	# this location is in percentage.
	desiredLeftEye=(0.35, 0.35)
	#Set the croped image(face) size after rotaion.
	#desiredFaceWidth = desiredWidth		#128
	#desiredFaceHeight = desiredHeight	#128

	desiredRightEyeX = 1.0 - desiredLeftEye[0]
	 
	# determine the scale of the new resulting image by taking
	# the ratio of the distance between eyes in the *current*
	# image to the ratio of distance between eyes in the
	# *desired* image
	dist = np.sqrt((dX ** 2) + (dY ** 2))
	desiredDist = (desiredRightEyeX - desiredLeftEye[0])
	desiredDist *= desiredFaceWidth
	scale = desiredDist / dist

	# compute center (x, y)-coordinates (i.e., the median point)
	# between the two eyes in the input image
	eyesCenter = ((leftEyeCenter[0] + rightEyeCenter[0]) // 2,
		(leftEyeCenter[1] + rightEyeCenter[1]) // 2)

	# grab the rotation matrix for rotating and scaling the face
	M = cv2.getRotationMatrix2D(eyesCenter, angle, scale)

	# update the translation component of the matrix
	tX = desiredFaceWidth * 0.5
	tY = desiredFaceHeight * desiredLeftEye[1]
	M[0, 2] += (tX - eyesCenter[0])
	M[1, 2] += (tY - eyesCenter[1])

	# apply the affine transformation
	(w, h) = (desiredFaceWidth, desiredFaceHeight)
	(y2,x2,y1,x1) = face_locations[0] 
			
	output = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC)
	return output

image0=face_recognition.load_image_file("../../images/test/obama_and_biden.jpg")
#image=cv2.imread('images/kit_with_rose.jpg')
image=cv2.cvtColor(image0,cv2.COLOR_BGR2RGB)
face_locations = face_recognition.face_locations(image)
print("Rostro 1")
print("yr1, xr1 yr2 xr2")
print(face_locations[0])
print("Rostro 2")
print("yr3, xr3 yr4 xr4")
print(face_locations[1])
print("Rostro 3")
print("yr5, xr5 yr6 xr6")
print(face_locations[2])
#68 ptos de referencia de la imagen
#face_landmarks = face_recognition.face_landmarks(image)
#alinear el rostro
# after alignment we have to resize the image so we have to give 
# width and height of the output aligned face.
cv2.imshow('image',image)
cv2.waitKey(0)
i=0
for face_location in face_locations:
	(top,right,bottom,left) = face_location 
	
	imagec0=image[top:bottom,left:right]
	cv2.imshow('imagec'+str(i),imagec0)
	cv2.waitKey(0)
	i+=1
	
	
desiredWidth = (right-left) 
desiredHeight = (bottom-top)
#print(face_landmarks)
#alignf=alignFace(image, face_locations, face_landmarks, desiredWidth, desiredHeight)


#entra a la red neuronal

#print(len(face_encoding))

#cv2.imshow('image',image1)
#cv2.waitKey(0)
#cv2.imshow('image',alignf)
#cv2.waitKey(0)
cv2.destroyAllWindows()

	
