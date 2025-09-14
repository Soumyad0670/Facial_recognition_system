import cv2
import face_recognition
import pickle
from utils import load_images_from_folder

def encode_known_faces(known_faces_dir='known_faces', encodings_path='encodings.pickle'):
    known_images, known_labels = load_images_from_folder(known_faces_dir)

    known_face_encodings = []
    known_face_names = []

    for img, label in zip(known_images, known_labels):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img_rgb)
        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(label)
    
    # Save to disk using pickle
    with open(encodings_path, 'wb') as f:
        pickle.dump({'encodings': known_face_encodings, 'names': known_face_names}, f)
    print(f"Encodings saved to {encodings_path}")

if __name__ == '__main__':
    encode_known_faces()
