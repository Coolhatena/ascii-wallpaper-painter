import cv2
import numpy as np

img_name = 'image1.png'

img = cv2.imread(img_name,  cv2.IMREAD_UNCHANGED)
height, width, depth = img.shape
img_res = img.copy()
print(img[0][0])


for i, row in enumerate(img):
	for j, px in enumerate(row):
		_, _, _, alpha = px
		if alpha != 0:
			img_res[i][j] = np.array([255, 255, 255, 255])

cv2.imwrite('result.png', img_res)


