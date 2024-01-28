# Proyecto de Monitoreo de Temperatura, Humedad y Giroscopio con Arduino y Python

Bienvenido al repositorio del proyecto de monitoreo de temperatura, humedad y datos del giroscopio utilizando Arduino y Python. Este proyecto te permite construir y desplegar un sistema de recopilación y visualización de datos ambientales en tiempo real.

## Contenido del Repositorio

- **DatosArduino.ino**: Este archivo contiene el código para Arduino, donde se configura la lectura del sensor DHT y del módulo MPU, así como la transmisión de datos a través del puerto serial.

- **PostDatos.py**: Este script en Python se encarga de recolectar datos desde el puerto serial de Arduino, formatearlos y enviarlos a una base de datos en Azure mediante un request POST en formato JSON.

- **GraficarDatos.py**: Este script en Python utiliza el método GET para recuperar los datos almacenados en la base de datos y generar dos gráficas. Una muestra la evolución de la temperatura y la humedad, mientras que la otra representa los datos del giroscopio en los ejes x, y, y z.

## Uso

1. Ejecuta `PostDatos.py` para comenzar la recopilación y envío de datos desde Arduino a Azure.

2. Después, ejecuta `GraficarDatos.py` para generar las gráficas de temperatura, humedad y datos del giroscopio.

3. ¡Explora y analiza tus datos en tiempo real!

Si tienes alguna pregunta o sugerencia, no dudes en contribuir al proyecto. ¡Disfruta monitoreando y visualizando tus datos ambientales!
