import cv2
import serial
import time

# Conectá al puerto COM de tu ESP32
arduino = serial.Serial('COM11', 9600)
time.sleep(2)  # Espera a que el microcontrolador inicie

# Detector Haar de caras (integrado en OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        print("Cara detectada")
        arduino.write(b'1')  # Enviar "1"
    else:
        print("Sin cara")
        arduino.write(b'0')  # Enviar "0"

    # Mostrar video
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Detector Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
arduino.close()
cv2.destroyAllWindows()
