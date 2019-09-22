import cv2
import numpy as np

img = cv2.imread('chris.jpg', 1)

img = cv2.line(img, (50.50), (100,100), (255,0,0), 3)

cv2.imshow(img)

if cv2.waitKey(0) == ord('s'):
    cv2.imwrite('cool dude but with line', img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()




