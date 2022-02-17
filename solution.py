# import socket module
from socket import *
# In order to terminate the program
import sys
from urllib import request

host = '127.0.0.1' 
port = 13331
def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind((host, port))
  #Fill in start
  serverSocket.listen(1)

  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
    try:

      try:
        message =  connectionSocket.recv(1024).decode() #Fill in start    #Fill in end
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start     #Fill in end
        
        #Send one HTTP header line into socket.
        #Fill in start
        response = 'HTTP/1.9 200 OK\n\nHello World'
        connectionSocket.sendall(response.encode())
        connectionSocket.close()
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        while True: 
            headers = request.split('\n')
            filename = headers[0].split()[1]

            if filename == '/':
                filename = '/index.html'
            try: 
                f = open('htdocs'+filename)
                outputdata = f.read()
                f.close()

                message = 'HTT/1.0 200 OK\n\n' + outputdata
            except FileNotFoundError:
                message = 'HTTP/1.0 404 Not Found\n\nFile Not Found'
            connectionSocket.sendall(message.encode())
            connectionSocket.close()

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
