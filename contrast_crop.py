import numpy as np
from skimage import data, color, exposure
from skimage.io import imread, imsave
from skimage.transform import rescale, rotate
from skimage.feature import canny, peak_local_max
from scipy import ndimage as ndi
from skimage.viewer import ImageViewer
from scipy.ndimage.filters import convolve
from skimage.transform import hough_circle
from skimage.draw import circle_perimeter
import os, math

categories = ['10rp', '1fr', '20rp', '2fr', '50rp', 'fr', 'rp']

for category in categories:
	for filename in os.listdir('data/'+ category):
		if filename.endswith('.png') and not filename.endswith('-cropped.png'):
		    img = imread('data/' + category + '/' + filename, as_grey=True)
		    for n in range(10):
		        img2 = rotate(img, n * 36)
		        img2 = img2[img2.shape[0] / 4:img2.shape[0] * 3 / 4, img2.shape[1] / 4:img2.shape[1] * 3 / 4]
		        img2 = exposure.equalize_hist(img2)
		        imsave('data/' + category + '/' + filename[:-4] + '-' + str(n) + '-cropped.png', img2)
