import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
image = cv2.imread("crowd.jpeg")


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.putText(image, "Number of faces detected: " + str(len(faces)), (0, image.shape[0] - 10),
            cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()