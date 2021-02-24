from socket import *

debug = False

def log(message):
    if debug:
        print (message)


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    #Prepare a client socket connection
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    log("~Connection requested to server. Response: " + recv)
    if recv[:3] != '220':
        log('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    log("~HELO Response: " + recv1)
    if recv1[:3] != '250':
        log('250 reply not received from server. For command: ' + heloCommand)

    # Send MAIL FROM command and print server response.
    command = 'MAIL FROM: <an3391@nyu.edu>\r\n'
    clientSocket.send(command.encode())
    recvrep = clientSocket.recv(1024).decode()
    log("~MAIL FROM Response: " + recvrep)
    if recvrep[:3] != '250':
        log('250 reply not received from server. For command: ' + command)

    # Send RCPT TO command and print server response.
    command = 'RCPT TO: <namsinbox@gmail.com>\r\n'
    clientSocket.send(command.encode())
    recvrep = clientSocket.recv(1024).decode()
    log("~RCPT TO Response: " + recvrep)
    if recvrep[:3] != '250':
        log('250 reply not received from server. For command: ' + command)

    # Send DATA command and print server response.
    command = 'DATA\r\n'
    clientSocket.send(command.encode())
    recvrep = clientSocket.recv(1024).decode()
    log("~DATA Response: " + recvrep)
    if recvrep[:3] != '354':
        log('354 reply not received from server. For command: ' + command)

    # Send message data.
    command = 'This is my message. PL!\r\n'
    clientSocket.send(command.encode())

    # Message ends with a single period.
    command = '.\r\n'
    clientSocket.send(command.encode())
    recvrep = clientSocket.recv(1024).decode()
    log("~message Response: " + recvrep)
    if recvrep[:3] != '250':
        log('250 reply not received from server. For command: ' + command)

    # Send QUIT command and get server response.
    command = 'QUIT\r\n'
    clientSocket.send(command.encode())
    recvrep = clientSocket.recv(1024).decode()
    log("~QUIT Response: " + recvrep)
    if recvrep[:3] != '221':
        log('221 reply not received from server. For command: ' + command)


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')