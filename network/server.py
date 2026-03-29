import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

s.bind((host,port))
s.listen(5)

client, address = s.accept()
print("Connection from: " + str(address))
while True:
    message = input("Enter message to send to client: ")
    client.send(message.encode('utf-8'))

    message_from_client = client.recv(250)
    print("Message from client: " + message_from_client.decode('utf-8'))

