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

training_images = [
    "DSC08315",
    "DSC08316",
    "DSC08319",
    "DSC08320",
    "DSC08321"
]

for training_image in training_images:
    original_image = imread("data/photos/" + training_image + ".jpg", as_grey=True)

    image = rescale(original_image, 1200.0 / len(original_image))

    edges = canny(image, sigma=0.7)

    kernel = np.array(5 * [5*[1]])

    edges = convolve(edges, kernel)

    fill = ndi.binary_fill_holes(edges)

    edges = canny(fill)

    hough_radii = np.arange(50, 150, 5)
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
            if (c[0] - center_y) * (c[0] - center_y) + (c[1] - center_x) * (c[1] - center_x) < (c[2] + radius) * (c[2] + radius) * 0.25:
                add = False
                break
        if add:
            circles.append([center_y, center_x, radius])

    #print len(circles)

    #image = color.gray2rgb(image)

    #for circle in circles:
    #    cx, cy = circle_perimeter(*circle)
    #    image[cy, cx] = (220, 20, 20)

    #ve = ImageViewer(image)
    #ve.show()

    i = 0
    for c in circles:
        circle_img = image[c[1] - c[2]:c[1] + c[2], c[0] - c[2]:c[0] + c[2]]
        imsave("data/coins/" + training_image + "_" + str(i) + ".png", circle_img)
        i += 1
