import cv2
import numpy as np

img = cv2.imread('chris.jpg', 1)

img = cv2.rectangle(img, (1100, 500), (2300, 1800), (0, 0, 255), 20)
font = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img, 'target', (1100, 400), font, 8, (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow('image', img)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('cool dude but with line.jpg', img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
