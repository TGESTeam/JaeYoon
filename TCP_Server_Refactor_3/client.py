import socket
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to the server.")

        try:
            while True:
                message = input("Enter message to send to server: ")
                if message.lower() == 'exit':
                    break
                
                client_socket.sendall(message.encode())
                data = client_socket.recv(BUFFER_SIZE)
                print(f"Received from server: {data.decode()}")
                
                time.sleep(1)  # Optional delay between messages
        except KeyboardInterrupt:
            print("Client disconnected.")
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
