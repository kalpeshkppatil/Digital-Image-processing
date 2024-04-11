# ----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
import cv2
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
first_image = cv2.imread(r'C:\Users\Idrees\Desktop\1.tif',0)
#-----------------------------------------------------------------------------#
plt.imshow(first_image, cmap='gray')
plt.axis('off')
plt.show()
# image in frequency domain
F = np.fft.fft2(first_image)
plt.imshow(np.log1p(np.abs(F)),cmap='gray')
plt.axis('off')
plt.show()
#-----------------------------------------------------------------------------#
#              after shfiting the frequencies to center                       #
#-----------------------------------------------------------------------------# 
Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)),cmap='gray')
plt.axis('off')
plt.show()
# #-----------------------------------------------------------------------------#
# #                             Ideal Low pass Filter (ILPF)
# #-----------------------------------------------------------------------------#
M,N = first_image.shape
H = np.zeros((M,N), dtype=np.float32)
D0 = 100
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        if D <= D0:
            H[u,v] = 1
        else:
            H[u,v] = 0
            
plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()
# # it will show low pass flter that we programmed above
# #-----------------------------------------------------------------------------#
# #   Applying Ideal low pass filter to an image in frequency domain            #
# #=============================================================================#

Gshift = Fshift * H
plt.imshow(np.log1p(np.abs(Gshift)),cmap='gray')
plt.axis('off')
plt.show()
# #  this is the fitered image in the frequency domain
# #-----------------------------------------------------------------------------#
# #     Inverse Fourier Tranform                                                #
# #=============================================================================#
G = np.fft.ifftshift(Gshift)
plt.imshow(np.log1p(np.abs(G)),cmap='gray')
plt.axis('off')
plt.show()
# # since we shifted the low frequencies from origin to center
# # Therefore, we have to shift back them to origins/corners
# # inorder to get filtered image back in spatial domain
# #-----------------------------------------------------------------------------#
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()

# # above code takes the inverse Fourier tranform to get back our digital image int
# # spatial domain
# #-----------------------------------------------------------------------------#
# #                        Ideal High Pass Filter                               #
# #=============================================================================#
# H = 1 - H
# # plt.imshow(H, cmap='gray')
# # plt.axis('off')
# # plt.show()
# #-----------------------------------------------------------------------------#
# Gshift = Fshift * H
# # plt.imshow(np.log1p(np.abs(Gshift)),cmap='gray')
# # plt.axis('off')
# # plt.show()
# #-----------------------------------------------------------------------------#
# #                          Inverse Fourier Transform
# #-----------------------------------------------------------------------------#
# G = np.fft.ifftshift(Gshift)
# # plt.imshow(np.log1p(np.abs(G)),cmap='gray')
# # plt.axis('off')
# # plt.show()
# #-----------------------------------------------------------------------------#g = np.abs(np.fft.ifft2(G))
# plt.imshow(g, cmap='gray')
# plt.axis('off')
# plt.show()