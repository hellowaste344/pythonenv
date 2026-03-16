import cv2  # type: ignore

src = cv2.imread(r"logo.jpg")

"""
cv2.COLOR_BGR2GRAY BGR: Grayscale
cv2.COLOR_BGR2RGB BGR: RGB
cv2.COLOR_BGR2HSV BGR: HSV
cv2.COLOR_BGR2LAB BGR: LAB color space
"""
cv2.imshow("BGR logo", src)
# opencv reads image in BGR format not RGB
rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB logo ", rgb)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV logo ", hsv)

lab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB logo ", lab)

cv2.waitKey(0)
