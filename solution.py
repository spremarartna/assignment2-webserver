# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a server socket
    serverSocket.bind(("", port))
    #Fill in start
    host = "localhost"
    port = 13331
    serverSocket.listen(1)
    print('Lisenting on port %s....' % port)
    #Fill in end

    while True:
        #Establish the connection
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
        try:

            try:
                message = connectionSocket.recv(1024).decode('utf-8') #Fill in start    #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read() #Fill in start     #Fill in end
                print(outputdata)

                #Send one HTTP header line into socket.
                #Fill in start
                message = 'HTTP/1.1 200 OK\n\nHello World'
                connectionSocket.sendall(message.encode())
                #Fill in end

                #Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                #Fill in start
                message = 'HTTP/1.1 404 File Not Found\n\nFile Not Found'
                connectionSocket.sendall(message.encode())
                #Fill in end


             #Close client socket
            #Fill in start
                connectionSocket.close()
            #Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

            serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
