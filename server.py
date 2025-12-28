from socket import socket, AF_INET, SOCK_STREAM

server=socket(AF_INET,SOCK_STREAM)
server.bind(("localhost",8000))
server.listen()
client_connect,adresse = server.accept()
client_connect.sendall("Connexion établie".encode())


while True :
    message = input("Entrez votre message: ")
    client_connect.sendall(message.encode())
    if message == "quit" : break

    out = client_connect.recv(512).decode()
    print(out)
    if out == "quit":
        break





server.close()