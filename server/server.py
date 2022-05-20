from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from person import Person

#constant global variables
HOST = "localhost"
PORT = 3000
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

MAX_CONNECTIONS = 5
BUFSIZ = 512

#global variables
persons = []


def broadcast(msg, name):
    for person in persons:
        client = person.client
        client.send(bytes(name, "utf8") + msg)

def client_communication(person):
    client = person.client

    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)
    persons.append(person)
    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, name + ": ")

    while True:
        try:
            msg = client.recv(BUFSIZ).decode("utf8")
            if msg=="quit":
                msg = bytes(f"{name} has left the chat!", "utf8")
                client.close()
                persons.remove(person)
                broadcast(msg, name + ":")
                print(f"[LOGGING]: {person.addr} has disconnected")
                break
            else:
                print(name+": "+msg)
                broadcast(bytes(msg,"utf8"), name+": ")

        except Exception as e:
            print(f"[EXCEPTION-cc]: {e}")
            break


def wait_for_connections():
    while True:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            print(f"[LOGGING]: {addr} has connected")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print(f"[EXCEPTION-wfc]: {e.message}")
            break
    print("SERVER STOPPED")


if __name__=="__main__":
    SERVER.listen(MAX_CONNECTIONS)
    print("[Starting]: Waiting for connection")
    ACCEPT_THREAD = Thread(target=wait_for_connections, args=())
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()