import dlib
import cv2
import matplotlib.pyplot as plt

# Ruta del modelo pre-entrenado para predecir puntos de referencia
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Crear un detector de rostros HOG usando la clase incorporada de dlib
face_detector = dlib.get_frontal_face_detector()

# Cargar el modelo para predecir puntos de referencia faciales
face_pose_predictor = dlib.shape_predictor(predictor_model)

# Ruta de la imagen en la que deseas graficar los puntos de referencia
ruta_imagen = "imgppt.jpg"

# Cargar la imagen con OpenCV
imagen = cv2.imread(ruta_imagen)

# Convertir la imagen a escala de grises (dlib requiere imágenes en escala de grises)
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen
caras_detectadas = face_detector(imagen_gris)

# Recorrer todas las caras detectadas y graficar los puntos de referencia en la imagen
for cara in caras_detectadas:
    # Obtener los puntos de referencia faciales
    puntos_faciales = face_pose_predictor(imagen_gris, cara)

    # Convertir los puntos de referencia a coordenadas (x, y) y graficarlos en la imagen
    for i in range(68):
        x = puntos_faciales.part(i).x
        y = puntos_faciales.part(i).y
        cv2.circle(imagen, (x, y), 3, (255, 255, 255), -1)  # Dibujar un círculo verde en cada punto

    # Obtener las coordenadas del rectángulo que rodea el rostro detectado
    x_min, y_min, x_max, y_max = cara.left(), cara.top(), cara.right(), cara.bottom()

    # Dibujar un rectángulo alrededor del rostro detectado
    #cv2.rectangle(imagen, (x_min, y_min), (x_max, y_max), (255, 255, 255), 3)  # Rectángulo azul

# Mostrar la imagen con los puntos de referencia graficados
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Desactivar ejes para mostrar solo la imagen
plt.show()