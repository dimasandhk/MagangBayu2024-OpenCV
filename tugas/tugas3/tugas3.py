import cv2
import numpy as np
from mss import mss
import pyautogui as pg

# program deteksi pola tiles
# sangat terinspirasi dari video vincoo
# https://youtu.be/RlTkCrrO4ek?si=d-qFe423cArHZ-LO

# Define the bounding box of the screen or window
bounding_box = {'top': 400, 'left': 803, 'width': 930, 'height': 900}
sct = mss()

lower = np.array([0, 0, 0])
upper = np.array([30, 0, 0])
pg.PAUSE = 0.1

while True:
    # Capture the screen
    sct_img = sct.grab(bounding_box)
    # Convert the screenshot to a numpy array and then to a color image
    img = cv2.cvtColor(np.array(sct_img), cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1], reverse=True)

    cv2.imshow("Mask", mask)
    if len(contours) != 0:
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255, 0), 2)
            x_location = round((x+(w/4)))

            tx = bounding_box['width'] - bounding_box['left'] + 800
            ty = bounding_box['height'] - bounding_box['top'] - 200

            pg.click(x_location + tx, y+(h) + ty, 1, 0)

    # If 'q' is pressed on the keyboard, break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break