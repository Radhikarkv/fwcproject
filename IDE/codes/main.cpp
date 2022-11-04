#include<Arduino.h>

int clockPin =13;
byte leds=0;

void setup()
{
  pinMode(clockPin, OUTPUT);
}
void loop()
{
  leds = 0;
  digitalWrite(clockPin,HIGH);
  delay(1500);
  for (int i = 0; i < 4; i++)
  {
    bitSet(leds, i);
    delay(1500);
    digitalWrite(clockPin,LOW);
  }
}


