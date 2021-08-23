const float pi = 3.14;
int contador = 0;
bool dato = LOW;
bool datoAnterior = LOW;
float tiempoAnterior = 0;
float tiempo = 0;
float diferencia = 0;
float velocidad = 0;
float w = 0;

void setup() {
pinMode(2,INPUT);
Serial.begin(9600);
}

void loop() {
 dato = digitalRead(2);
 if (dato == HIGH && datoAnterior == LOW)
 {
  tiempo=millis();
  contador++;
  diferencia = tiempo-tiempoAnterior;
  tiempoAnterior=tiempo;
  w=(2*pi)/(diferencia/1000);
  velocidad=w*0.152; // dimensiones anemometro 
  Serial.println("T");
  Serial.println(diferencia);
  Serial.println("Velocidad");
  Serial.println(velocidad);
  
 }
 datoAnterior = dato;
}
