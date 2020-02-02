import face_recognition
image_me = face_recognition.load_image_file('me.jpg')
image_me2 = face_recognition.load_image_file('me2.jpg')
image_sean = face_recognition.load_image_file('notme.jpg')
image_chrispratt = face_recognition.load_image_file('chrispratt.jpeg')
image_katyperry = face_recognition.load_image_file('katyperry.jpg')

me_encoding = face_recognition.face_encodings(image_me)[0]
me2_encoding = face_recognition.face_encodings(image_me2)[0]
sean_encoding = face_recognition.face_encodings(image_sean)[0]
chrispratt_encoding = face_recognition.face_encodings(image_chrispratt)[0]
katyperry_encoding = face_recognition.face_encodings(image_katyperry)[0]

known_faces = [sean_encoding, chrispratt_encoding, me2_encoding,
            katyperry_encoding]

results = face_recognition.compare_faces(known_faces, me_encoding)
num = 0
for i in results:
    num = num + 1
    if i == True:
        print("Photo", num, "is a photo of Hannah!")
