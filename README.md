# 🧠 Detector Facial + LED con ESP32

Este proyecto usa Python y OpenCV para detectar rostros con la cámara web. Si se detecta una cara, se envía una señal por puerto serial al ESP32, que prende un LED. Si no hay rostro, el LED se apaga.

## 🔧 Requisitos

- Python 3 con `opencv-python` y `pyserial`
- ESP32 (o Arduino)
- LED + resistencia
- Arduino IDE para cargar el código
