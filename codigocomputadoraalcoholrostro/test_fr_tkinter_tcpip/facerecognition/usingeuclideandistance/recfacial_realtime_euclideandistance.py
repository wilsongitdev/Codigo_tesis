import face_recognition
import pickle
import cv2
# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.
with open('encodingfaces.txt', 'rb') as f:
    data = pickle.load(f)

encodings = data[0]
labels = data[1]
# print(encodings)
# print("------")
# print(labels)

webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 480)
font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 255, 255)
grosor = 2
while (True):

    ret, test_image = webcam.read()
    facelocations = face_recognition.face_locations(test_image, 1, 'hog')
    if len(facelocations) == 1:
        (top, right, bottom, left) = facelocations[0]
        # Predict all the faces in the test_fr_tkinter_tcpip image using the trained classifier

        test_image_enc = face_recognition.face_encodings(test_image, facelocations, 1, 'small')[0]

        result = face_recognition.compare_faces(encodings, test_image_enc,0.6)
        if True in result:
            index = result.index(True)
            idperson = labels[index]

        print(idperson)
        # cv2.rectangle(test_image, (left, top), (right, bottom), color, grosor)
        # cv2.putText(test_image, nombre, (left + 50, top - 90), font, 1, color, grosor, cv2.LINE_AA)
        # cv2.putText(test_image, str(max(prob[0]))[0:6], (left + 50, top - 60), font, 1, color, grosor, cv2.LINE_AA)
        cv2.imshow('Imagen', test_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("No se ha detectado rostro")

webcam.release()
cv2.destroyAllWindows()

# # Load some images to compare against
# known_obama_image = face_recognition.load_image_file("obama.jpg")
# known_biden_image = face_recognition.load_image_file("biden.jpg")
#
# # Get the face encodings for the known images
# obama_face_encoding = face_recognition.face_encodings(known_obama_image)[0]
# biden_face_encoding = face_recognition.face_encodings(known_biden_image)[0]
#
# known_encodings = [
#     obama_face_encoding,
#     biden_face_encoding
# ]
#
# # Load a test_fr_tkinter_tcpip image and get encondings for it
# image_to_test = face_recognition.load_image_file("obama2.jpg")
# image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]
#
# # See how far apart the test_fr_tkinter_tcpip image is from the known faces
# face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
#
# for i, face_distance in enumerate(face_distances):
#     print("The test_fr_tkinter_tcpip image has a distance of {:.2} from known image #{}".format(face_distance, i))
#     print("- With a normal cutoff of 0.6, would the test_fr_tkinter_tcpip image match the known image? {}".format(face_distance < 0.6))
#     print("- With a very strict cutoff of 0.5, would the test_fr_tkinter_tcpip image match the known image? {}".format(face_distance < 0.5))
#     print()