import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.connect((host, port))

while True:
    message = s.recv(250)
    print("Message from server: " + message.decode('utf-8'))

    message_to_send = input("Enter message to send to server: ")
    s.send(message_to_send.encode('utf-8'))