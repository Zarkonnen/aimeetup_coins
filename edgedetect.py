import numpy as np
from skimage.io import imread
from skimage.transform import rescale
from skimage.feature import canny
from scipy import ndimage as ndi
from skimage.viewer import ImageViewer
from scipy.ndimage.filters import convolve

image = rescale(imread("data/photos/DSC08315.jpg", as_grey=True), 0.5)

edges = canny(image, sigma=0.7)

kernel = np.array(5 * [5*[1]])

edges = convolve(edges, kernel)

fill = ndi.binary_fill_holes(edges)

ve = ImageViewer(fill)
ve.show()
