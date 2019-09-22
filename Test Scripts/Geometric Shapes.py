import cv2
import numpy as np

img = cv2.imread('chris.jpg', 1)

img = cv2.line(img, (50, 50), (2000, 2000), (100, 100, 0), 10)

cv2.imshow('image', img)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('cool dude but with line.jpg', img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
