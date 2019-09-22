import cv2

#### Read and Write Photos
##image = cv2.imread('chris.jpg', 0) # Gray Scale
##
##print(image)
##
##cv2.imshow('cool dude', image)
##key = cv2.waitKey()
##
##if key == 27:
##    cv2.destroyAllWindows()
##elif key == ord('s'):
##    cv2.imwrite('cool dude but gray.png', image)
##    cv2.destroyAllWindows()


### Video Capture
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', frame_gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
