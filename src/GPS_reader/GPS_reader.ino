
void setup() {
    Serial.begin(9600);
    Serial1.begin(38400); // Lecture du port série TX/RX
}

void loop() {
    char c = 0;
    while (Serial1.available())
    {
        c = Serial1.read();
    }
}