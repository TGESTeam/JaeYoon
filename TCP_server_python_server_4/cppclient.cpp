#include <iostream>
#include <string>
#include <cstring>
#include <arpa/inet.h>
#include <unistd.h>

#define SERVER_HOST "127.0.0.1"
#define SERVER_PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char buffer[BUFFER_SIZE] = {0};

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        std::cout << "Socket creation error." << std::endl;
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(SERVER_PORT);

    //IP주소를 연결하기 위한 함수이며 inet_pton이 IP주소를 이진형식으로 변환 serv_addr.sin_addr 여기에 저장함
    if (inet_pton(AF_INET, SERVER_HOST, &serv_addr.sin_addr) <= 0) {
        std::cout << "Invalid address/ Address not supported." << std::endl;
        return -1;
    }

    if (connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        std::cout << "Connection Failed." << std::endl;
        return -1;
    }

    std::string message;
    while (true) {
        std::cout << "Enter message to send to server (type 'exit' to quit): ";
        std::getline(std::cin, message);
        if (message == "exit") {
            break;
        }

        send(sock, message.c_str(), message.size(), 0);
        int valread = read(sock, buffer, BUFFER_SIZE);
        if (valread > 0) {
            std::cout << "Received from server: " << std::string(buffer, valread) << std::endl;
        }
    }

    close(sock);
    return 0;
}
