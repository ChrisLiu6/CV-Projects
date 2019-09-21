import cv2
import face_recognition
from matplotlib import pyplot as plt
import face_recognition

known_image = face_recognition.load_image_file("steve.jpg")
unknown_image = face_recognition.load_image_file("unknown2.jpg")

##face_landmarks_list = face_recognition.face_landmarks(image)
##face_locations = face_recognition.face_locations(image)

steve_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([steve_encoding], unknown_encoding)
##plt.imshow(face_locations)
##plt.show()
