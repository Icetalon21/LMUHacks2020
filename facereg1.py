import face_recognition

def face_recognition1(photo1, photo2, photo3, photo4, photo5, photo6):
    image_test = face_recognition.load_image_file(photo1)
    image_two = face_recognition.load_image_file(photo2)
    image_three = face_recognition.load_image_file(photo3)
    image_four = face_recognition.load_image_file(photo4)
    image_five = face_recognition.load_image_file(photo5)
    image_six = face_recognition.load_image_file(photo6)

    test_encoding = face_recognition.face_encodings(image_test)[0]
    two_encoding = face_recognition.face_encodings(image_two)[0]
    three_encoding = face_recognition.face_encodings(image_three)[0]
    four_encoding = face_recognition.face_encodings(image_four)[0]
    five_encoding = face_recognition.face_encodings(image_five)[0]
    six_encoding = face_recognition.face_encodings(image_six)[0]

    known_faces = [two_encoding, three_encoding, four_encoding,
                    five_encoding, six_encoding]
    results = face_recognition.compare_faces(known_faces, test_encoding)
    num = 0
    for i in results:
        num = num + 1
        if i == True:
            print("Photo", num, "is a photo of Hannah!")

one = input("Enter test photo: ")
two = input("Enter photo one: ")
three = input("Enter photo two: ")
four = input("Enter photo three: ")
five = input("Enter photo four: ")
six = input("Enter photo five: ")
face_recognition1(one, two, three, four, five, six)
