
/*
  1. Arduino receives acknowledgement letter 'a' from computer on serial communication.
  2. After receiving the acknowledgement letter 'a', arduino sends 'value1' to computer
  3. The above process is repeated for four values in this example.
*/
int value1 = 11;
int value2 = 22;
int value3 = 33;
int value4 = 44;

void setup() {
  Serial.begin(9600);       // starting the serial communication, baud rate = 9600
}

void loop() {
  if (Serial.available() > 0) {
    int inByte = Serial.read();       // reading the data from serial port
    switch (inByte) {
      case 'a':                       // if received 'a' from computer
        Serial.println(value1);       // send 'value1' to the computer   
        break;                        // get out of loop, check again for serial connection and read serial port
      case 'b':
        Serial.println(value2);
        break;
      case 'c' :
        Serial.println(value3);
        break;
      case 'd':
        Serial.println(value4);
        break;
      default:
        Serial.println("00");
    }
  }
}
