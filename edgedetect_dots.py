import numpy as np
from skimage import data, color
from skimage.io import imread, imsave
from skimage.transform import rescale
from skimage.feature import canny, peak_local_max
from scipy import ndimage as ndi
from skimage.viewer import ImageViewer
from scipy.ndimage.filters import convolve
from skimage.transform import hough_circle
from skimage.draw import circle_perimeter

original_image = imread("Voting sheet pictures/tailoredmotor.jpg", as_grey=True)

image = rescale(original_image, 800.0 / len(original_image))

edges = canny(image, sigma=1)

kernel = np.array(15 * [15*[1]])

edges = convolve(edges, kernel)

#fill = ndi.binary_fill_holes(edges)

edges = canny(edges)

hough_radii = np.arange(30, 60, 3)
hough_res = hough_circle(edges, hough_radii)

centers = []
accums = []
radii = []

for radius, h in zip(hough_radii, hough_res):
    num_peaks = 20
    peaks = peak_local_max(h, num_peaks=num_peaks)
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

circles = []
for idx in np.argsort(accums)[::-1][:100]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    add = True
    for c in circles:
        if (c[0] - center_y) * (c[0] - center_y) + (c[1] - center_x) * (c[1] - center_x) < (c[2] + radius) * (c[2] + radius) * 0.7:
            add = False
            break
    if add:
        circles.append([center_y, center_x, radius])

print len(circles)

image = color.gray2rgb(image)

for circle in circles:
    cx, cy = circle_perimeter(*circle)
    image[cy, cx] = (220, 20, 20)

ve = ImageViewer(image)
ve.show()