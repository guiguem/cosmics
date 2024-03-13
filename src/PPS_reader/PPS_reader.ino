

int TTL_PIN = 8; // pull high to output
int PAUSE = 2000;
void setup() {
    Serial.begin(9600);
    Serial.println("here");
    pinMode(TTL_PIN, INPUT);
}
void loop() {
    if (digitalRead(TTL_PIN)) {
        Serial.println("high");
    // do this if C2 is high
    }
    else {
        Serial.println("low");

    }
    // digitalRead(TTL_PIN);
    // delay(PAUSE);
    // digitalWrite(TTL_PIN, HIGH);
    delay(100);
    // Serial.println("loop");
} 