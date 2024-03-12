import socket

ESP_IP = 'ESP_IP_ADDRESS'  # Replace with the actual IP address of your ESP8266

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((ESP_IP, 8080))
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        print('Response:', response)

if __name__ == "__main__":
    print("Enter commands to control Arduino. Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter a command (e.g., 'digitalWrite(13, HIGH)'): ")
        
        if user_input.lower() == 'exit':
            break

        send_command(user_input)
