import socket
import RPi.GPIO as GPIO

led_pin = 14

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Define the IP address and port number for the server
HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 1234

# Create a socket object and bind to the specified address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Waiting for connection...")
# Wait for a client to connect
client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

# Loop to receive and process messages
while True:
    # Receive a message from the client
    message = client_socket.recv(1024).decode().strip()

    # If the message is "on", turn the light on
    if message == "ENABLE":
        print("Turning light on")
        GPIO.output(led_pin, GPIO.HIGH)

    # If the message is "off", turn the light off
    elif message == "DISABLE":
        print("Turning light off")
        GPIO.output(led_pin, GPIO.LOW)

    # If the message is something else, print an error message
    else:
        print("Unknown command")

# End this client
client_socket.close()
print("Disconnected from client, waiting for new one...")

# Clean up GPIO and close the socket when done
GPIO.cleanup()
server_socket.close()
