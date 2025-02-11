

int TTL_PIN = 8; // pull high to output
int PAUSE = 2000;
void setup() {
    Serial.begin(9600);
    Serial.println("here");
    pinMode(TTL_PIN, OUTPUT);
}
void loop() {
    digitalWrite(TTL_PIN, LOW);
    delay(PAUSE);
    digitalWrite(TTL_PIN, HIGH);
    delay(10);
    Serial.println("loop");
} 