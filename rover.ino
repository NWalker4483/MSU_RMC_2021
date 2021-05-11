#include <SoftwareSerial.h>

#define TIMEOUT 2

#define LEFT 0
#define RIGHT 128

#define CW 0
#define CCW 64

SoftwareSerial ControlA(8, 10); // RX, TX
SoftwareSerial ControlB(9, 11); // RX, TX

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
    delay(1);
  };
  theNumberString[numberOfDigits] = 0x00;
  theNumber = atoi(theNumberString);
  return theNumber;
}

void loop() {
  // reply only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    byte incomingByte = Serial.read();
    switch (incomingByte) {
    case 'A':
      int speed = parseIntFast(4);
      speed = constrain(speed, -100, 100);
      int cmd = LEFT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlA.write(cmd);
      break;
    case 'B':
      int speed = parseIntFast(4);
      speed = constrain(speed, -100, 100);
      int cmd = RIGHT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlA.write(cmd);
      break;
    case 'C':
      int speed = parseIntFast(4);
      speed = constrain(speed, -100, 100);
      int cmd = LEFT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlB.write(cmd);
      break;
    case 'D':
      int speed = parseIntFast(4);
      speed = constrain(speed, -100, 100);
      int cmd = RIGHT;
      cmd += (speed < 0) ? CCW : CW;
      cmd += map(abs(speed), 0, 100, 0, 63);
      ControlB.write(cmd);
      break;
    default:
      // do something
    }
  }
}