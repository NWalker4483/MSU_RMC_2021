#include <SoftwareSerial.h>

#define TIMEOUT 2

#define LEFT 0
#define RIGHT 128

#define CW 0
#define CCW 64

SoftwareSerial ControlA(8, 10); // RX, TX
SoftwareSerial ControlB(9, 11); // RX, TX

unsigned long lastRecieved[4];
void setup() {
  ControlA.begin(9600);
  ControlB.begin(9600);

  Serial.begin(9600);
}

int parseIntFast(int numberOfDigits) {
  /*
  This function returns the converted integral number as an int value.
  If no valid conversion could be performed, it returns zero.*/
  char theNumberString[numberOfDigits + 1];
  int theNumber;
  for (int i = 0; i < numberOfDigits; theNumberString[i++] = Serial.read()) {
    delay(2);
  };
  theNumberString[numberOfDigits] = 0x00;
  theNumber = atoi(theNumberString);
  return theNumber;
}

void loop() {
    unsigned long curr_time = millis(); // Stop motors individually 
    if ((curr_time - lastRecieved[0]) > TIMEOUT * 1000){
      ControlA.write((byte)LEFT); 
    }
    if ((curr_time - lastRecieved[1]) > TIMEOUT * 1000){
      ControlA.write((byte)RIGHT); 
    }
    if ((curr_time - lastRecieved[2]) > TIMEOUT * 1000){
      ControlB.write((byte)LEFT); 
    }
    if ((curr_time - lastRecieved[3]) > TIMEOUT * 1000){
      ControlB.write((byte)RIGHT); 
    }    
  // reply only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    byte incomingByte = Serial.read();
    int cmd, speed;

      speed = parseIntFast(4);
      speed = constrain(speed, -100, 100);
    switch (incomingByte) {
    case 'A':
      cmd = LEFT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlA.write((byte)cmd);
      lastRecieved[0] = curr_time;
      break;
    case 'B':
      cmd = RIGHT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlA.write((byte)cmd);
      lastRecieved[1] = curr_time;
      break;
    case 'C':
      cmd = LEFT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlB.write((byte)cmd);
      lastRecieved[2] = curr_time;
      break;
    case 'D':
      cmd = RIGHT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlB.write((byte)cmd);
      lastRecieved[3] = curr_time;
      break;
   
    }
  }
}
