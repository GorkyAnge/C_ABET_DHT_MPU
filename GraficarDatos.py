import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, clear_output
import time
import requests

api_url = 'http://apiproductos20240125082039.azurewebsites.net/api/Datos' 
giroscopio_x = []
giroscopio_y = []
giroscopio_z = []
temperatura = []
humedad = []
muestras = []

# Función para obtener datos desde la API
def get_data_from_api():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción para errores HTTP

        data_list = response.json()

        # Limpiamos las listas antes de agregar nuevos datos
        temperatura.clear()
        humedad.clear()
        giroscopio_x.clear()
        giroscopio_y.clear()
        giroscopio_z.clear()
        muestras.clear()

        if data_list:
            for data in data_list:
                temp = data.get('temperatura')
                hum = data.get('humedad')
                gyro_x = data.get('giroX')
                gyro_y = data.get('giroY')
                gyro_z = data.get('giroZ')

                if temp is not None and hum is not None and gyro_x is not None and gyro_y is not None and gyro_z is not None:
                    print(f"Datos recibidos de la API: Temperatura={temp}, Humedad={hum}, GiroX={gyro_x}, GiroY={gyro_y}, GiroZ={gyro_z}")

                    # Agregar datos a las listas
                    temperatura.append(temp)
                    humedad.append(hum)
                    giroscopio_x.append(gyro_x)
                    giroscopio_y.append(gyro_y)
                    giroscopio_z.append(gyro_z)
                    muestras.append(len(muestras) + 1)

            # Graficar después de obtener todos los datos
            update_plot()

    except requests.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")


def update_plot():

    # Configuración inicial de la gráfica
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    axs[0].set_xlabel('Muestras')
    axs[0].set_ylabel('Valor')
    axs[0].set_title('Gráfica Temperatura vs Humedad')
    axs[1].set_xlabel('Muestras')
    axs[1].set_ylabel('Valor')
    axs[1].set_title('Gráfica Giroscopio X, Y, Z')

    # Actualizar datos de las líneas
    axs[0].plot(muestras, temperatura, label='Temperatura', color='red')
    axs[0].plot(muestras, humedad, label='Humedad', color='blue')
    axs[1].plot(muestras, giroscopio_x, label='Giroscopio X', color='green')
    axs[1].plot(muestras, giroscopio_y, label='Giroscopio Y', color='orange')
    axs[1].plot(muestras, giroscopio_z, label='Giroscopio Z', color='purple')

    plt.tight_layout()
    plt.show()
    plt.pause(0.01)
    clear_output(wait=True)  # Limpiar la salida para evitar superposiciones


while True:
    get_data_from_api()
    time.sleep(1)
