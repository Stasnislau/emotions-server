from deepface import DeepFace


face_analysis = DeepFace.analyze(img_path="woman.jpg", enforce_detection=False)

print(face_analysis[0]["dominant_emotion"])