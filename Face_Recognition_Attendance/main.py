# main.py - Capture faces and log names
import cv2
import face_recognition
import os

print("🎓 Starting Smart Attendance...")

known_face_encodings = []
known_face_names = []

# Load known faces from folder
for name in os.listdir("students"):
    image = face_recognition.load_image_file(f"students/{name}")
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(os.path.splitext(name)[0])

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            name = known_face_names[matches.index(True)]
            print(f"Present: {name}")

    cv2.imshow('Attendance', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()