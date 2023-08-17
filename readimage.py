import cv2
img = cv2.imread("butterfly.jpg")

cv2.imshow("Display Image",img)

print(img)
cv2.waitKey(0)