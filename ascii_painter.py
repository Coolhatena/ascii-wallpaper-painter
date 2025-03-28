import cv2

img_name = 'notext.png'
img = cv2.imread(img_name, cv2.IMREAD_UNCHANGED)

mask = img[:, :, 3] != 0

img[mask] = [255, 255, 255, 255]

cv2.imwrite(f'result_{img_name}', img)


