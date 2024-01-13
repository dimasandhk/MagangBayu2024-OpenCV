import cv2
import numpy as np

lower = np.array([80, 60, 65])
upper = np.array([90, 170, 185])

img = cv2.imread("tugas1.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_img, lower, upper)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Result", img)
cv2.imwrite("tugas1_res.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()