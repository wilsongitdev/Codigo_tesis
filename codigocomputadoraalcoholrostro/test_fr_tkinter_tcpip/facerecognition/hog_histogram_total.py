import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_hog_descriptor(window):
    # Definir los parámetros del HOG
    win_size = (64, 128)  # Tamaño de la ventana
    block_size = (16, 16)  # Tamaño del bloque
    block_stride = (8, 8)  # Desplazamiento del bloque
    cell_size = (8, 8)  # Tamaño de la celda
    nbins = 9  # Número de bins del histograma

    # Crear el HOG Descriptor
    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)

    # Calcular el descriptor HOG de la ventana
    hog_descriptor = hog.compute(window)

    return hog_descriptor

if __name__ == "__main__":
    # Cargar la imagen (aquí debes cargar tu imagen real)
    image = cv2.imread("imgppt.jpg", cv2.IMREAD_GRAYSCALE)

    # Definir las coordenadas de la ventana de interés (por ejemplo, con esquina superior izquierda en (100, 100))
    x, y = 100, 100
    window_size = (64, 128)  # Tamaño de la ventana

    # Extraer la ventana de la imagen
    window = image[y:y+window_size[1], x:x+window_size[0]]

    # Calcular el descriptor HOG de la ventana
    hog_descriptor = compute_hog_descriptor(window)

    # Convertir el descriptor HOG en un array de NumPy y ajustar los ángulos al rango de 0 a 180 grados
    hog_array = np.squeeze(hog_descriptor) % 180

    # Normalizar el descriptor HOG
    hog_array = hog_array / 2  # Dividir por 2 para obtener los ángulos en el rango correcto de 0 a 180 grados
    hog_array /= np.sum(hog_array)

    # Graficar el histograma
    plt.bar(range(len(hog_array)), hog_array)
    plt.xlabel('Bin del histograma')
    plt.ylabel('Frecuencia normalizada')
    plt.title('Histograma normalizado del descriptor HOG (0-180 grados)')
    plt.show()
