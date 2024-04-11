import cv2
import numpy as np
from matplotlib import pyplot as plt


#-----------------------------------------------------------------------------#

img = cv2.imread(r'C:\Users\Idrees\Desktop\Everyting\MIT-WPU\Semester-IV\DIP\Lab_Programs\Images\Chapter3\Fig0320(1)(top_left).tif',0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Digital Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Corresponding Frequency Domain'), plt.xticks([]), plt.yticks([])
plt.show()