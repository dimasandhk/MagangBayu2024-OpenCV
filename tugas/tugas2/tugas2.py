import cv2
import numpy as np

img = cv2.imread("tugas2.jpg")
x_start, y_start = 200, 650
cropped_img = img[x_start:500, y_start:900]

blur = cv2.GaussianBlur(cropped_img, (5, 5), 100)

lower = np.array([0, 0, 0])
upper = np.array([255, 100, 30])

mask = cv2.inRange(blur, lower, upper)
canny = cv2.Canny(mask, 10, 25)

contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

for contour in contours:
    shifted_contour = contour + [y_start, x_start]
    cv2.drawContours(img, [shifted_contour], -1, (0, 0, 0), 4)
    epsilon = 0.02 * cv2.arcLength(shifted_contour, True)
    approx = cv2.approxPolyDP(shifted_contour, epsilon, True)

    cv2.putText(img, str(len(approx)), (10, 125), cv2.FONT_HERSHEY_SIMPLEX , 5, (0, 0, 0), 2, cv2.LINE_AA) 

cv2.imshow("Result", img)
cv2.imwrite("tugas2_res.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()