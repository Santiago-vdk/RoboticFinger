#include <Servo.h>


int servoPin = 3;

Servo servo;  
 
int servoAngle = 0;   // servo position in degrees

String inData;

int motor1_dir_pin = 52;
int motor1_step_pin = 50;
int motor1_enable_pin = 48;

int motor2_dir_pin = 53;
int motor2_step_pin = 51;
int motor2_enable_pin = 49;

int microsteps = 3200;     //3200 - 360 grados

void setup() 
{
  pinMode(motor1_dir_pin, OUTPUT);     // Pin que maneja la direccion del motor 1
  pinMode(motor1_step_pin, OUTPUT);    // Pin que maneja el step del motor 1
  pinMode(motor1_enable_pin, OUTPUT);  // Pin que maneja la activacion del motor 1
  
  pinMode(motor2_dir_pin, OUTPUT);     // Pin que maneja la direccion del motor 2
  pinMode(motor2_step_pin, OUTPUT);    // Pin que maneja el step del motor 2
  pinMode(motor2_enable_pin, OUTPUT);  // Pin que maneja la activacion del motor 2
  
  digitalWrite(motor1_enable_pin, HIGH); // Iniciamos el motor 1 apagado (Evita sonido agudo de bobina)
  digitalWrite(motor2_enable_pin, HIGH); // Iniciamos el motor 1 apagado (Evita sonido agudo de bobina)
  servo.attach(servoPin);
  
  Serial.setTimeout(50);
  Serial.begin(9600);    // USB serial port 0
  Serial3.begin(9600);   // serial port 3


}


void loop()
{
  int i;
  
  while (Serial.available() > 0) {
    
    char recieved = Serial.read();
    inData += recieved; 

    

    // Process message when new line character is recieved
    if (recieved == '\n')
    {
        //Serial.print("Arduino Received: ");
        //Serial.print(inData);
      

        String operacion = inData.substring(0, inData.indexOf('_'));
        inData = inData.substring(inData.indexOf('_') + 1, inData.length());
        
        String steps = inData.substring(0, inData.indexOf('_'));
        
        
        if(operacion == "000" & steps.length() > 0){
          //Serial.print("Rotando M1 hacia la izquierda\n");
          // Escribir a servo gemelo
          String instruccion = "$000_";
          String eof = "%";
          String mensaje = "";
          mensaje.concat(instruccion);
          steps.trim();
          mensaje.concat(steps);
          mensaje.concat(eof);
          
          //Serial.print(mensaje);
          
          Serial3.write(mensaje.c_str());
          
          digitalWrite(motor1_enable_pin, LOW);
    
          digitalWrite(motor1_dir_pin, HIGH);     // Set the direction.
          delay(100);
          int steps_int = steps.toInt();
          for (i = 0; i<steps_int; i++)       // Iterate for 4000 microsteps.
          {
            digitalWrite(motor1_step_pin, LOW);  // This LOW to HIGH change is what creates the
            digitalWrite(motor1_step_pin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
            delayMicroseconds(500);      // This delay time is close to top speed for this
          }
          
          digitalWrite(motor1_enable_pin, HIGH);  
          
          
        } else if(operacion == "001" & steps.length() > 0){
          //Serial.print("Rotando M1 hacia la derecha\n");
          // Escribir a servo gemelo
          String instruccion = "$001_";
          String eof = "%";
          String mensaje = "";
          mensaje.concat(instruccion);
          steps.trim();
          mensaje.concat(steps);
          mensaje.concat(eof);
          
          //Serial.print(mensaje);
          
          Serial3.write(mensaje.c_str());
          
          digitalWrite(motor1_enable_pin, LOW);
    
          digitalWrite(motor1_dir_pin, LOW);     // Set the direction.
          delay(100);
        
          int steps_int = steps.toInt();
          for (i = 0; i<steps_int; i++)       // Iterate for 4000 microsteps.
          {
            digitalWrite(motor1_step_pin, LOW);  // This LOW to HIGH change is what creates the
            digitalWrite(motor1_step_pin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
            delayMicroseconds(500);      // This delay time is close to top speed for this
          }
          
          digitalWrite(motor1_enable_pin, HIGH);  
     
        } else if(operacion == "010" & steps.length() > 0){
          //Serial.print("Rotando M2 hacia la izquierda\n");
          
          digitalWrite(motor2_enable_pin, LOW);
    
          digitalWrite(motor2_dir_pin, LOW);     // Set the direction.
          delay(100);
        
          int steps_int = steps.toInt();
          for (i = 0; i<steps_int; i++)       // Iterate for 4000 microsteps.
          {
            digitalWrite(motor2_step_pin, LOW);  // This LOW to HIGH change is what creates the
            digitalWrite(motor2_step_pin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
            delayMicroseconds(500);      // This delay time is close to top speed for this
          }
          
          digitalWrite(motor2_enable_pin, HIGH);  
     
        } else if(operacion == "011" & steps.length() > 0){
          //Serial.print("Rotando M2 hacia la derecha\n");
          
          digitalWrite(motor2_enable_pin, LOW);
    
          digitalWrite(motor2_dir_pin, HIGH);     // Set the direction.
          delay(100);
        
          int steps_int = steps.toInt();
          for (i = 0; i<steps_int; i++)       // Iterate for 4000 microsteps.
          {
            digitalWrite(motor2_step_pin, LOW);  // This LOW to HIGH change is what creates the
            digitalWrite(motor2_step_pin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
            delayMicroseconds(500);      // This delay time is close to top speed for this
          }
          
          digitalWrite(motor2_enable_pin, HIGH);  
     
        }  else if(operacion == "100" & steps.length() > 0){
          //Serial.print("Rotando dedo\n");
 
          // Desplazamos a la posición 180º
          servo.write(100);
          // Esperamos 1 segundo
          //delay(steps.toInt()*1000);
          delay(300);
           // Desplazamos a la posición 0º
          servo.write(0);
 
 
        }
        
        else {
          Serial.print("Operacion Desconocida\n");
        }
        
        inData = ""; // Clear recieved buffer
    }
    
  }
}

