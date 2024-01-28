# Proyecto de Monitoreo de Temperatura, Humedad y Giroscopio con Arduino y Python

Bienvenido al repositorio del proyecto de monitoreo de temperatura, humedad y datos del giroscopio utilizando Arduino y Python. Este proyecto te permite construir y desplegar un sistema de recopilación y visualización de datos ambientales en tiempo real.

## Contenido del Repositorio

- **DatosArduino.ino**: Este archivo contiene el código para Arduino, donde se configura la lectura del sensor DHT y del módulo MPU, así como la transmisión de datos a través del puerto serial.

- **PostDatos.py**: Este script en Python se encarga de recolectar datos desde el puerto serial de Arduino, formatearlos y enviarlos a una base de datos en Azure mediante un request POST en formato JSON.

- **GraficarDatos.py**: Este script en Python utiliza el método GET para recuperar los datos almacenados en la base de datos y generar dos gráficas. Una muestra la evolución de la temperatura y la humedad, mientras que la otra representa los datos del giroscopio en los ejes x, y, y z.

## Configuración del Entorno

1. **Arduino Setup**: Carga el código en el Arduino y asegúrate de tener correctamente conectados el sensor DHT y el módulo MPU a la protoboard.

2. **Azure Database Configuration**: Configura tu base de datos en Azure y actualiza las credenciales en el script `data_collector.py` para asegurar la conexión correcta.

3. **Dependencias de Python**: Asegúrate de tener instaladas las bibliotecas necesarias. Puedes instalarlas ejecutando `pip install -r requirements.txt` en tu entorno virtual.

## Uso

1. Ejecuta `PostDatos.py` para comenzar la recopilación y envío de datos desde Arduino a Azure.

2. Después, ejecuta `GraficarDatos.py` para generar las gráficas de temperatura, humedad y datos del giroscopio.

3. ¡Explora y analiza tus datos en tiempo real!

Si tienes alguna pregunta o sugerencia, no dudes en contribuir al proyecto. ¡Disfruta monitoreando y visualizando tus datos ambientales!
