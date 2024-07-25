import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
BUFFER_SIZE = 1024

def start_server():
    # 서버 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()

    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}...")

    while True:
        client_socket, addr = server_socket.accept()
        print("접속한 클라이언트의 주소 입니다. : ", addr)

        # 클라이언트와의 통신
        handle_client(client_socket)

def handle_client(client_socket):
    while True:
        try:
            string = client_socket.recv(BUFFER_SIZE).decode()
            if not string:
                break
            print(f"받은 데이터는 \"{string}\" 입니다.")

            # 클라이언트에게 받은 데이터를 그대로 다시 보냄
            client_socket.sendall(string.encode())
        except ConnectionResetError:
            print("클라이언트 연결이 종료되었습니다.")
            break

    print("접속을 종료합니다.")
    client_socket.close()

if __name__ == "__main__":
    start_server()


# import socket
# import time

# SERVER_HOST = '127.0.0.1'
# SERVER_PORT = 8080
# BUFFER_SIZE = 1024

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# server_socket.bind((SERVER_HOST,SERVER_PORT))

# server_socket.listen()

# client_socket, addr = server_socket.accept()

# print("접속한 클라이언트의 주소 입니다. : ", addr)

# while 1:
#     string = client_socket.recv(1024).decode()
#     if string == "": break
#     print("받은 데이터는 \"", string, "\" 입니다.", sep="")

#     client_socket.sendall(string.encode())
# # 소켓을 닫는다.
# print("접속을 종료합니다.")
# client_socket.close()
# server_socket.close()
