from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Lock
from time import time

class Client:
    HOST = "localhost"
    PORT = 3000
    ADDR = (HOST, PORT)
    BUFSIZ = 512
    def __init__(self, name) -> None:
        self.name = name
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.receive_thread = Thread(target=self.receive_messages)
        self.receive_thread.start()
        self.messages = []
        self.lock = Lock()
        self.send_message(name)

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ)
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
                #print(msg)
            except Exception as e:
                print(f"[EXCEPTION] {e}")
                break

    def send_message(self,msg):
        print(f'{self.client_socket}: {msg}')
        self.client_socket.send(bytes(msg, "utf8"))
        if msg=="quit":
            self.client_socket.close()

    def get_messages(self):
        message_copy = self.messages[:]
        self.lock.acquire()
        self.messages = []
        self.lock.release()
        return message_copy
    
    def disconnect(self):
        self.send_message("quit")
