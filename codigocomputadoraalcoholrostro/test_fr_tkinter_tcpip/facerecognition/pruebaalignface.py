import cv2

web_cam = cv2.VideoCapture(1)

_, imagen = web_cam.read()

cv2.imwrite("images/wilsonvolteado.jpg", imagen)
cv2.imshow("Gaaaa", imagen)
# Cuando todo está hecho, liberamos la captura
cv2.waitKey(0)
web_cam.release()
cv2.destroyAllWindows()

