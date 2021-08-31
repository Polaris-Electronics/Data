//Anemometro
const float pi = 3.14;
int contador = 0;
bool dato = LOW;
bool datoAnterior = LOW;
float tiempoAnterior = 0;
float tiempo = 0;
float diferencia = 0;
float velocidad = 0;
float w = 0;

//Giroscopio
#include "I2Cdev.h"
#include "MPU6050.h"
#include "Wire.h"
MPU6050 sensor;
int ax, ay, az;
int gx, gy, gz;

// Temperatura
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
 



void setup() {
  pinMode(3,INPUT);
  pinMode(2,INPUT);
  Serial.begin(9600);
  dht.begin();
  Wire.begin();            
  sensor.initialize();

  
  if (sensor.testConnection()) Serial.println("Sensor iniciado correctamente");
  else Serial.println("Error al iniciar el sensor");
}

void loop() {
  //delay(5000);
 
//temperatura
  float h = dht.readHumidity();
  
  float t = dht.readTemperature();
 
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Error obteniendo los datos del sensor DHT11");
    return;
  }
 
 
  float hif = dht.computeHeatIndex(f, h);
  
  float hic = dht.computeHeatIndex(t, h, false);
 

 //Anemometro

 dato = digitalRead(3);
 if (dato == HIGH && datoAnterior == LOW)
 {
  tiempo=millis();
  contador++;
  diferencia = tiempo-tiempoAnterior;
  tiempoAnterior=tiempo;
  w=(2*pi)/(diferencia/1000);
  velocidad=w*0.152; // dimensiones anemometro 

  
 }
 datoAnterior = dato;
 

  //Prints
  //Humedad
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("##");
//Temperatura
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print("##");
 //Indice de calor

  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print("##");
// Anemometro
 //Tiempo
  
  Serial.print(diferencia);
  
  Serial.print("##");
 //Velocidad
  Serial.print(velocidad);
  
  Serial.print("##");
//Giroscopio
  sensor.getAcceleration(&ax, &ay, &az);
  sensor.getRotation(&gx, &gy, &gz);
  Serial.print(ax); 
  Serial.print(ay); 
  Serial.print(az);
  Serial.print("##");
  Serial.print(gx);
  Serial.print(" ");
  Serial.print(gy);
  Serial.print(" ");
  Serial.print(gz);
  Serial.print(" "); 
  Serial.print("##");
  Serial.println();
  delay(100);
    
}
