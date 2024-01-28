import requests
import serial
import json

ser = serial.Serial('COM3', 9600)

while True: 
    line = ser.readline().decode('utf-8').strip()
    if line:
        temperature, gyroZ, gyroX, gyroY, humidity = map(float, line.split())
        url = "https://apiproductos20240125082039.azurewebsites.net/api/Datos"
        data = {
            "idDatos": 0,
            "temperatura": temperature,
            "humedad": humidity,
            "giroX": gyroX,
            "giroY": gyroY,
            "giroZ": gyroZ,
        }
        headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    print(response.status_code)
    print(response.text)
