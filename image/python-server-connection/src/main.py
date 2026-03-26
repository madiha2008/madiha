import socket
import sys
from config import SERVER_ADDRESS, SERVER_PORT

def main():
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to the server
            client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
            print(f"Connected to server at {SERVER_ADDRESS}:{SERVER_PORT}")

            # Main loop to send and receive data
            while True:
                message = input("Enter message to send (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    print("Exiting...")
                    break

                # Send message to the server
                client_socket.sendall(message.encode())
                print("Message sent!")

                # Receive response from the server
                response = client_socket.recv(1024)
                print(f"Received from server: {response.decode()}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()