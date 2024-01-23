import numpy as np
import cv2
import matplotlib.pyplot as plt


def compute_gradients(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the gradients in the x and y directions
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the magnitude and angle of the gradients
    magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
    angle = np.degrees(np.arctan2(grad_y, grad_x))

    # Adjust angles to be in the range of 0 to 180 degrees
    angle = np.mod(angle, 180)

    return magnitude, angle


def compute_histogram(magnitude, angle, num_bins):
    # Calculate the histogram of gradient orientations
    histogram = np.zeros(num_bins)
    bin_range = 180 / num_bins
    for i in range(num_bins):
        lower_bound = i * bin_range
        upper_bound = (i + 1) * bin_range
        mask = np.logical_and(angle >= lower_bound, angle < upper_bound)
        histogram[i] = np.sum(magnitude[mask])

    # Check if the histogram has a sum of zero or contains NaN or infinite values
    if np.sum(histogram) == 0 or np.isnan(histogram).any() or np.isinf(histogram).any():
        # If the histogram cannot be normalized, return zeros
        histogram = np.zeros_like(histogram)
    else:
        # Normalize the histogram
        histogram /= np.sum(histogram)

    return histogram


def compute_hog_block(image_block, num_bins=9, cell_size=8):
    # Compute the gradients of the image block
    magnitude, angle = compute_gradients(image_block)

    # Split the block into cells and calculate the histograms for each cell
    cell_histograms = []
    for i in range(0, image_block.shape[0], cell_size):
        for j in range(0, image_block.shape[1], cell_size):
            cell_magnitude = magnitude[i:i + cell_size, j:j + cell_size]
            cell_angle = angle[i:i + cell_size, j:j + cell_size]
            cell_histogram = compute_histogram(cell_magnitude, cell_angle, num_bins)
            cell_histograms.append(cell_histogram)

    # Concatenate the cell histograms to form the final block HOG descriptor
    hog_block = np.concatenate(cell_histograms)

    return hog_block


# Example usage
if __name__ == "__main__":
    # Load an example image
    image_path = "imgppt.jpg"
    image = cv2.imread(image_path)

    # Define the block size and cell size
    block_size = 16  # In pixels
    cell_size = 8  # In pixels

    # Select a block from the image
    block_start_x, block_start_y = 100, 100
    block_end_x, block_end_y = block_start_x + block_size, block_start_y + block_size
    block = image[block_start_y:block_end_y, block_start_x:block_end_x]

    # Compute the HOG descriptor for the selected block
    hog_descriptor = compute_hog_block(block, num_bins=9, cell_size=cell_size)

    # Create an array for the bin centers in degrees (from 0 to 180)
    bin_centers = np.arange(0, 180, 180 / len(hog_descriptor))

    # Display the HOG descriptor as a bar graph
    plt.bar(bin_centers, hog_descriptor, width=180 / len(hog_descriptor))
    print(len(bin_centers))
    plt.title("Descriptor del bloque normalizado (HOG)")
    plt.xlabel("Orientación (grados)")
    plt.ylabel("Magnitud")
    plt.show()