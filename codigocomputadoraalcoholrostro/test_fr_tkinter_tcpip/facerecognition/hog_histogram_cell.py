import cv2
import numpy as np
import matplotlib.pyplot as plt


def calculate_gradient_histogram(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate gradients in x and y directions using Sobel operator
    gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the magnitude and direction (in radians) of the gradients
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    # Convert the radians to degrees and map them to the range [0, 180]
    gradient_direction_degrees = np.degrees(gradient_direction) % 180

    # Calculate the histogram of gradient angles with 9 bins
    histogram, bins = np.histogram(gradient_direction_degrees, bins=9, range=(0, 180))

    # Center the angles for plotting
    bin_centers = (bins[:-1] + bins[1:]) / 2.0

    return histogram, bin_centers


# Load the image (replace 'image_path' with the path to your image file)
image_path = 'imgppt.jpg'
image = cv2.imread(image_path)
image = image[8:408, 8:408]
#hog a toda la imagen rectangular
#image = image[0:200, 0:400]
# hog a una celda
image = image[0:8, 0:8]
# Calculate the gradient histogram
histogram, angles = calculate_gradient_histogram(image)

# Plot the histogram
plt.bar(angles, histogram, width=20, align='center')
plt.title('Histograma de gradientes', fontsize=15)
plt.xlabel('Orientación (grados)', fontsize=13)
plt.ylabel('Frecuencia', fontsize=13)
plt.show()
