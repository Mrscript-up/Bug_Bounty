#include <iostream>
#include <string>
#include <vector>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

bool scanPort(const std::string& targetIp, int port) {
    
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        return false;
    }
  
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(port); 
    
    if (inet_pton(AF_INET, targetIp.c_str(), &serverAddr.sin_addr) <= 0) {
        close(sockfd);
        return false;
    }

       
    int connectionStatus = connect(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
    
    close(sockfd);  

    return connectionStatus == 0;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <IP Address>\n";
        std::cerr << "Example: " << argv[0] << " 192.168.1.1\n";
        return 1;
    }

    std::string targetIp = argv[1];
    
    
    std::vector<int> commonPorts = {
        21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 
        993, 995, 3306, 3389, 5432, 8080, 8443
    };

    std::cout << "[*] Starting scan on host: " << targetIp << "\n";
    std::cout << "--------------------------------------------------\n";

    int openPortsCount = 0;
    for (int port : commonPorts) {
        std::cout << "Scanning port " << port << "...\r";
        std::cout.flush();  

        if (scanPort(targetIp, port)) {
            std::cout << "[+] Port " << port << " is OPEN!              \n";
            openPortsCount++;
        }
    }

    std::cout << "--------------------------------------------------\n";
    std::cout << "[*] Scan finished. Found " << openPortsCount << " open ports.\n";

    return 0;
}
