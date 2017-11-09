String inData;

int motor1_dir_pin = 2;
int motor1_step_pin = 3;
int motor1_enable_pin = 4;

int microsteps = 3200;     //3200 - 360 grados

void setup() 
{
  pinMode(motor1_dir_pin, OUTPUT);     // Pin que maneja la direccion del motor 1
  pinMode(motor1_step_pin, OUTPUT);    // Pin que maneja el step del motor 1
  pinMode(motor1_enable_pin, OUTPUT);  // Pin que maneja la activacion del motor 1
  
  digitalWrite(motor1_enable_pin, HIGH); // Iniciamos el motor 1 apagado (Evita sonido agudo de bobina)
  
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
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
        Serial.print("Arduino Received: ");
        Serial.print(inData);


        String operacion = inData.substring(0, inData.indexOf('_'));
        inData = inData.substring(inData.indexOf('_') + 1, inData.length());
        
        /*String motor = inData.substring(0, inData.indexOf('_'));
        inData = inData.substring(inData.indexOf('_') + 1, inData.length());
        
        String direccion = inData.substring(0, inData.indexOf('_'));
        inData = inData.substring(inData.indexOf('_') + 1, inData.length());*/
        
        String steps = inData.substring(0, inData.indexOf('_'));
        
        
        if(operacion == "000" & steps.length() > 0){
          Serial.print("Rotando M1 hacia la izquierda\n");
          
          digitalWrite(motor1_enable_pin, LOW);
    
          digitalWrite(motor1_dir_pin, HIGH);     // Set the direction.
          delay(100);
          int steps_int = steps.toInt();
          for (i = 0; i<steps_int; i++)       // Iterate for 4000 microsteps.
          {
            digitalWrite(motor1_step_pin, LOW);  // This LOW to HIGH change is what creates the
            digitalWrite(motor1_step_pin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
            delayMicroseconds(150);      // This delay time is close to top speed for this
          }
          
          digitalWrite(motor1_enable_pin, HIGH);  
          
          
        } else if(operacion == "001" & steps.length() > 0){
          Serial.print("Rotando M1 hacia la derecha\n");
          
          digitalWrite(motor1_enable_pin, LOW);
    
          digitalWrite(motor1_dir_pin, LOW);     // Set the direction.
          delay(100);
        
          int steps_int = steps.toInt();
          for (i = 0; i<steps_int; i++)       // Iterate for 4000 microsteps.
          {
            digitalWrite(motor1_step_pin, LOW);  // This LOW to HIGH change is what creates the
            digitalWrite(motor1_step_pin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
            delayMicroseconds(150);      // This delay time is close to top speed for this
          }
          
          digitalWrite(motor1_enable_pin, HIGH);  
          
     
        } else {
          Serial.print("Operacion Desconocida\n");
        }
        
        inData = ""; // Clear recieved buffer
    }
    
  }
}

