import cv2
import numpy as np
img = cv2.imread("testimage2.png")
number_of_white_pix = np.sum(img == 255)  
print(number_of_white_pix+1)
