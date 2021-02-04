#import socket module
from socket import *
import sys # In order to terminate the program

debug = False

def log(message):
    if debug:
        print (message)

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    serverSocket.bind(("", port))
    #Fill in start
    serverSocket.listen(1)
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        #connectionSocket, addr = #Fill in start      #Fill in end
        connectionSocket, addr = serverSocket.accept()
        log ("connectionSocket:" + str(connectionSocket))
        log ("addr:" + str(addr))

        try:
            # message = # Fill in start    #Fill in end
            message = connectionSocket.recv(1024)
            log("message:" + str(message))

            filename = message.split()[1]
            log("filename:" + str(filename))

            # outputdata = #Fill in start     #Fill in end
            #
            # #Send one HTTP header line into socket
            # #Fill in start
            #
            # #Fill in end
            #

            if "helloworld.html" not in str(filename):
                outputdata = "HTTP/1.1 404 Not Found\n"
                log("outputdata:" + outputdata)
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                outputdata = "\n<html>404 Not Found</html>\n"
            else:
                outputdata = "HTTP/1.1 200 OK\n"
                log("outputdata:" + outputdata)
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                f = open(filename[1:])
                filedata = f.read()
                f.close()
                log("filedata:" + filedata)
                outputdata = "\n" + filedata + "\n"

            log("outputdata:" + outputdata)

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except Exception as e:
            log("Exception:" + str(e))
            #Send response message for file not found (404)
            #Fill in start

            #Fill in end

            #Close client socket
            #Fill in start

            #Fill in end
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)