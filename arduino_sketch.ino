int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    processCommand(command);
  }
}

void processCommand(String command) {
  Serial.println("Received command: " + command);

  if (command.startsWith("digitalWrite")) {
    int pin = command.substring(command.indexOf("(") + 1, command.indexOf(",")).toInt();
    int value = command.substring(command.indexOf(",") + 1, command.indexOf(")")).toInt();

    digitalWrite(pin, value);
    Serial.println("Command processed successfully.");
  }
}
