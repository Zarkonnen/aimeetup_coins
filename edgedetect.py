from skimage.io import imread
from skimage.transform import rescale
from skimage.feature import canny
from scipy import ndimage as ndi
from skimage.viewer import ImageViewer

image = rescale(imread("data/photos/DSC08315.jpg", as_grey=True), 0.1)

edges = canny(image)

fill = ndi.binary_fill_holes(edges)

vi = ImageViewer(image)
vi.show()

ve = ImageViewer(edges)
ve.show()

vf = ImageViewer(fill)
vf.show()
