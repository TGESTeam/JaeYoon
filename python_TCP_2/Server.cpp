#include <iostream>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main(){
    int server_fd, python_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("socket failed");
        exit(1);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)))
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(server_fd, 3) < 0){
        perror("listen failed");
        exit(EXIT_FAILURE);
    }

    if ((python_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0){
        perror("accept failed");
        exit(EXIT_FAILURE);
    }

    // 메시지 수신
    read(python_socket, buffer, BUFFER_SIZE);
    std::cout << "Message from client: " << buffer << std::endl;
    
    // 클라이언트로 메시지 전송
    const char *hello = "Hello from server";
    send(python_socket, hello, strlen(hello), 0);
    std::cout << "Hello message sent" << std::endl;
    
    close(python_socket);
    close(server_fd);
    return 0;
}