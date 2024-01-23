from ..webcam import *
from ..gpio import GPIO

def detectairflow():

	while True: 
		ret, image_webcam_bgr = cap.read() 
		#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.25)# permite la config de t_exp
		#cap.set(cv2.CAP_PROP_EXPOSURE,0.03)#texp entre 0 y 1
		#print(cap.get(cv2.CAP_PROP_EXPOSURE))
		cv2.waitKey(5)
		#print(f"GPIO.input(17) {GPIO.input(17)}")


		if GPIO.input(17) == False:
			break

	
	return image_webcam_bgr
