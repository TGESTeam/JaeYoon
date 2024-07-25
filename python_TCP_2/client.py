import socket

HOST = '127.0.0.1'  # 서버의 IP 주소
PORT = 8080         # 서버의 포트 번호

# 소켓 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 서버에 연결
    s.connect((HOST, PORT))
    
    # 서버로 메시지 전송
    message = "Hello from client"
    s.sendall(message.encode('utf-8'))
    print("Message sent to server")

    # 서버로부터 메시지 수신
    data = s.recv(1024)
    print(f"Message from server: {data.decode('utf-8')}")
