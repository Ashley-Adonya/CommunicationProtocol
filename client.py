
import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",8000))
print(client.recv(512).decode())


while True :

    out = client.recv(512).decode()
    print(out)
    if out=="quit":
        break
    message = input("Entrez votre message: ")
   
    client.sendall(message.encode())
    if message == "quit" :
        break


client.close()