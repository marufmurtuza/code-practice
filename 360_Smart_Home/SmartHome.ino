// CSE360 Project Code (FINAL)

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>

LiquidCrystal_I2C lcd(0x27, 20, 4); 

SoftwareSerial bluetooth(8 , 9);    
const int buzzerPin = 7;
const int flameSensorPin = 4; 
const int gasSensorPin = A0;
const int pirSensorPin = 6;

void alertLoop() {
  for (int i = 0; i < 50; i++) {
    digitalWrite(buzzerPin, HIGH);
    delay(100);
    digitalWrite(buzzerPin, LOW);
    delay(50);
  }
}

void setup() {
  Serial.begin(300);
  bluetooth.begin(9600); 
  lcd.init();
  lcd.begin(20, 4);        
  Serial.begin(300);
  lcd.backlight();         
  lcd.setCursor(0, 0);
  lcd.print("Smart Home System");
  delay(2000); 

   
  pinMode(buzzerPin, OUTPUT);
  pinMode(flameSensorPin, INPUT);
  pinMode(gasSensorPin, INPUT);
  pinMode(pirSensorPin, INPUT);
}

void loop() {
  Serial.print(bluetooth.read());
  int flameValue = digitalRead(flameSensorPin);
  int gasValue = analogRead(gasSensorPin);
  int pirValue = digitalRead(pirSensorPin);
  Serial.print("Flame: ");
  Serial.print(flameValue);
  Serial.print(" | Gas: ");
  Serial.print(gasValue);
  Serial.print(" | PIR: ");
  Serial.println(pirValue);
  if (pirValue == HIGH && flameValue == LOW) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
    lcd.setCursor(0, 2);
    lcd.print("Intruder & Fire Alert!");
    
    bluetooth.println("Intruder & Fire Alert!");
    delay(2000);
    alertLoop();
    delay(2000);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
  }

  if (flameValue == LOW && gasValue > 12 ) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
    lcd.setCursor(0, 2);
    lcd.print("Fire & Smoke Alert!");
    lcd.setCursor(0, 3);
    lcd.print("Please evacuate!");
    
    bluetooth.println("Fire & Smoke Alert! Please evacuate!");
    delay(2000);
    alertLoop();
    delay(2000);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
  }

  if (pirValue == HIGH && gasValue > 12 ) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
    lcd.setCursor(0, 2);
    lcd.print("Intruder & Smoke Alert!");
    
    bluetooth.println("Intruder & Smoke Alert!");
    delay(2000);
    alertLoop();
    delay(2000);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
  }

  else if (flameValue == LOW) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
    lcd.setCursor(0, 2);
    lcd.print("Fire Alert!");
    lcd.setCursor(0, 3);
    lcd.print("Please evacuate!");
    
    bluetooth.println("Fire Alert! Please evacuate!");
    delay(2000);
    alertLoop();
    delay(2000);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
  }

  else if (gasValue > 12 ) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
    lcd.setCursor(0, 2);
    lcd.print("Smoke Alert!");
    lcd.setCursor(0, 3);
    lcd.print("Please evacuate!");
    Serial.print(gasValue);
    
    bluetooth.println("Smoke Alert! Please evacuate!");
    delay(2000);
    alertLoop();
    delay(2000);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
  }

  else if (pirValue == HIGH) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
    lcd.setCursor(0, 2);
    lcd.print("Intruder Detected!");
    lcd.setCursor(0, 3);
    lcd.print("Calling For Help!");
    Serial.print(pirValue);
    
    bluetooth.println("Intruder Alert! Call for help!");
    delay(2000);
    alertLoop();
    delay(1000);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Smart Home System");
  }
  delay(1000);
}
