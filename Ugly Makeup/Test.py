from PIL import Image, ImageDraw
import sys
import numpy
import face_recognition
from matplotlib import pyplot as plt

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("test.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file("test.jpg")
    
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # Make the eyebrows into a nightmare
    d.polygon(face_landmarks['left_eyebrow'], fill=(255, 255, 0, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(255, 255, 0, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(255, 255, 0, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(255, 255, 0, 150), width=5)

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(0, 255, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(0, 255, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(0, 255, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(0, 255, 0, 64), width=8)

    # Sparkle the eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 0, 0, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 0, 0, 30))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(255, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(255, 0, 0, 110), width=6)

   
    pil_image.save('test.jpg')


