import socket
import RPi.GPIO as GPIO  # Assuming you are using a Raspberry Pi GPIO pin for LED control

LED_PIN = 18  # Replace with the actual GPIO pin you are using

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(1)
    print('Server listening on port 8080')

    while True:
        try:
            conn, addr = server.accept()
            print('Connected to', addr)

            data = conn.recv(1024).decode()
            if data:
                print('Received:', data)
                response = process_command(data)
                conn.send(response.encode())

            conn.close()
        except Exception as e:
            print(f"Error: {str(e)}")

def process_command(command):
    try:
        if command.startswith("digitalWrite"):
            _, pin, value = command.split(',')
            pin = int(pin.strip())
            value = int(value.strip())

            if pin == LED_PIN and value in [0, 1]:
                GPIO.output(pin, value)
                return f"Command '{command}' processed successfully."
            else:
                return f"Invalid pin or value for LED control: {command}"

        else:
            return f"Unknown command: {command}"

    except ValueError:
        return f"Invalid command format: {command}"

if __name__ == "__main__":
    setup_gpio()
    run_server()
