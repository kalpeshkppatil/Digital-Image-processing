#=========================================================#
#  How to transform digital image to a frequency domain  #
#--------------------------------------------------------#
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
#--------------------------------------------------------#


first_image = cv.imread(r'C:\Users\Idrees\Desktop\1.tif',0)
# cv.imshow('digital image', first_image)

#========================================================#
#   tranform image to a frequency domain                 #
#========================================================#
image_in_frequency_domain = np.fft.fft2(first_image)
plt.imshow(np.log1p(np.abs(image_in_frequency_domain)),cmap='gray')
Fshift = np.fft.fftshift(image_in_frequency_domain)
plt.imshow(np.log1p(np.abs(Fshift)),cmap='gray')


# cv.waitKey(0)
# cv.destroyAllWindows()