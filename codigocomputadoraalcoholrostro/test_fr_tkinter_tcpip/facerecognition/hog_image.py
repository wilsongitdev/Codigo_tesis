import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hog

def visualize_hog(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the HOG descriptor for the image
    _, hog_image = hog(gray, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, block_norm='L2-Hys')

    # Plot the original image and HOG image
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax1.set_title('Imagen de entrada')
    ax1.axis('off')

    ax2.imshow(hog_image, cmap='gray')
    ax2.set_title('Imagen HOG')
    ax2.axis('off')

    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = "img_ppt_2.png"
    visualize_hog(image_path)