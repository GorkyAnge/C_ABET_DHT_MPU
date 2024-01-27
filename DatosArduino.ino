#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 14
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
float temp = 0;
float humedad = 0;

Adafruit_MPU6050 mpu;

void setup(void) {
  Serial.begin(9600);

  dht.begin();
  while (!Serial)
    delay(10);

  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }

  Serial.println("");
  delay(100);
}

void loop() {
  sensors_event_t a, g, temp_mpu;
  float temp_dht, humedad;

  mpu.getEvent(&a, &g, &temp_mpu);
  temp_dht = dht.readTemperature();
  humedad = dht.readHumidity();

  Serial.println(temp_dht);
  Serial.print(" ");
  Serial.print(humedad);
  Serial.print(" ");
  Serial.print(g.gyro.x - 0.11);
  Serial.print(" ");
  Serial.print(g.gyro.y - 0.07);
  Serial.print(" ");
  Serial.print(g.gyro.z);
  Serial.print(" ");

  delay(5000);
}
