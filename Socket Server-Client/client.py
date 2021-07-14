import socket
import time
import threading
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.43.58"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    input()

if __name__ == "__main__":
    t1=threading.Thread(target=send, args=("Hello World!"),daemon=True)
    t1.start()
    t2=threading.Thread(target=send, args=("Hello Everyone!"),daemon=True)
    t2.start()
    send("Hello A2!")
    send(DISCONNECT_MESSAGE)