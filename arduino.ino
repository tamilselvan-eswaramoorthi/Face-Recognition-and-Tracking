#include <Servo.h>
Servo myservo;
#define LED 13
int pos=90;

void setup() {
  myservo.attach(10);
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        int serialListener = Serial.read()-64;
        if(serialListener == 3) {
        digitalWrite(LED, HIGH);
        pos=(pos+5);
        Serial.println(pos);
        }
        else 
        if (serialListener == 1) {
        digitalWrite(LED, LOW);
        pos=(pos-5);
                Serial.println(pos);

        }
        else{}
        myservo.write(pos);
 
        delay(20);
    }
}
