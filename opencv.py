import cv2

src = cv2.imread(r"logo.jpg")

"""
cv2.COLOR_BGR2GRAY BGR: Grayscale
cv2.COLOR_BGR2RGB BGR: RGB
cv2.COLOR_BGR2HSV BGR: HSV
cv2.COLOR_BGR2LAB BGR: LAB color space
"""
# opencv reads image in BGR format not RGB
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV logo ", hsv)

lab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB logo ", lab)

cv2.waitKey(0)
