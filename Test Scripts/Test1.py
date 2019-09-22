import cv2

image = cv2.imread('chris.jpg', 0) # Gray Scale

print(image)

cv2.imshow('cool dude', image)
key = cv2.waitKey()

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('cool dude but gray.png', image)
    cv2.destroyAllWindows()

