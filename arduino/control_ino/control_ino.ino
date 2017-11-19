#include <SoftwareSerial.h>

SoftwareSerial gtSerial(8, 7); // Arduino RX, Arduino TX

int motor1_dir_pin = 2;
int motor1_step_pin = 3;
int motor1_enable_pin = 4;

String inData;
void setup() 
{
  
     pinMode(motor1_dir_pin, OUTPUT);     // Pin que maneja la direccion del motor 1
  pinMode(motor1_step_pin, OUTPUT);    // Pin que maneja el step del motor 1
  pinMode(motor1_enable_pin, OUTPUT);  // Pin que maneja la activacion del motor 1
  

  digitalWrite(motor1_enable_pin, HIGH); // Iniciamos el motor 1 apagado (Evita sonido agudo de bobina)

  Serial.begin(9600);    // serial / USB port
  gtSerial.begin(9600);  // software serial port
}

byte rx_byte = 0;        // stores received byte
boolean mensaje = false;
void loop() {
  int i = 0;
  // check if byte available from USB port
  if (Serial.available()) {

    rx_byte = Serial.read();
    // send a byte to the software serial port
    gtSerial.write(rx_byte);
  }

  // check if byte available on the software serial port
  if (gtSerial.available()) {
    // get the byte from the software serial port
    //rx_byte = gtSerial.read();
    char recieved = gtSerial.read();
    
    if(mensaje == true && recieved != '%'){
      inData += recieved;
    }
    
    else if(recieved == '$'){
      mensaje = true;
     // inData += recieved;
      
    } else if(recieved == '%'){
        String operacion = inData.substring(0, inData.indexOf('_'));
        inData = inData.substring(inData.indexOf('_') + 1, inData.length());
        
        String steps = inData.substring(0, inData.indexOf('_'));
        
  
        if(operacion == "000" & steps.length() > 0){
          //Serial.print("Rotando M1 hacia la izquierda\n");
          
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
          
          
        } else if(operacion == "001" & steps.length() > 0){
          //Serial.print("Rotando M1 hacia la derecha\n");
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
     
        } 
      
      
      
      
      
      
      
      mensaje = false;
      inData = "";
      
    }
    
 
    
    
    Serial.write(rx_byte);
  }
}


