import requests
import cv2

webcam = cv2.VideoCapture(0)


# Set the URL of the target endpoint
url = 'https://proyectoalcohol.000webhostapp.com/proy_control_alc/user/Insertalcoholdata.php'

# Cargar img de la camara web
_, test_image = webcam.read()

# Convert the image to bytes using OpenCV's imencode() method
_, img_encoded = cv2.imencode('.jpg', test_image)


form_data = {
    'ing_alcohol': '1',
    'alc_mgl': '0.125',
    'alc_bac': '0.025',
    'dni': '74881892'
}

files = {
    "img": ("image.jpg", img_encoded, "image/jpeg")
}

# Send the image data using requests.post() method
response = requests.post(url, data=form_data, files=files)
output = response.text
webcam.release()
print('The response from the server is: \n', output)
