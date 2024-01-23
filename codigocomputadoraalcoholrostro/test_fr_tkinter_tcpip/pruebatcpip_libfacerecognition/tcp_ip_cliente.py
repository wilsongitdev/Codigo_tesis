import socket
import pickle
import cv2
import face_recognition
from sklearn import svm
from sklearn.metrics import accuracy_score
import os
"""

imgser=[1,2,3,4]

imgsercab=bytes(f"{len(imgser):<{HEADERSIZE}}", 'utf-8')
a=str(f"{len(imgser):<{HEADERSIZE}}")
print(a+"gaaa")
b=str(len(imgser))
print(b+"gaaa")
print("{:<10}".format(155)+"gaa")
if a==b:
	print("gaa")
"""
#########SVM
filename = '../../main/clasificadorid2.sav'
svm = pickle.load(open(filename, 'rb'))
#modulotcpip.configtcpip()
#########SOCKET
HEADERSIZE=10
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.11', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
	while True:
		img_ser_cab = b''
		new_msg = True
		while True:
			msg = sock.recv(16)

			if new_msg:

				msg_len = int(msg[:HEADERSIZE])
				print(msg_len)
				new_msg = False
			#print(f"full message length: {msglen}")
			img_ser_cab += msg
			
			if len(img_ser_cab)-HEADERSIZE == msg_len:
				print("mensaje recibido")
				imagendec = pickle.loads(img_ser_cab[HEADERSIZE:])
				#cv2.imshow('imagen',imagendec)
				#cv2.waitKey(0)
				new_msg = True
				img_ser_cab = b""
				
				##RECONOCIMIENTO FACIAL
				face_locations = face_recognition.face_locations(imagendec)
				# Predict all the faces in the test_fr_tkinter_tcpip image using the trained classifier
				test_image_enc = face_recognition.face_encodings(imagendec, face_locations)[0]
				name = svm.predict([test_image_enc])
				#post reconocimiento
				
				msgenv = sock.sendall(bytes(name[0], "utf-8"))
except:
	sock.close()


#print('sending {!r}'.format(message))
#sock.sendall(message)


