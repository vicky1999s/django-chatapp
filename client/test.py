from threading import Thread
import time
from myclient import Client

c1 = Client("vicky")
c2 = Client("Cat")


def update_messages():
    messages = []
    run = True
    while run:  
        time.sleep(1)
        new_msgs = c1.get_messages()
        messages.extend(new_msgs)
        for msg in new_msgs:
            print(msg)
            if msg=="quit":
                run = False
                break

Thread(target=update_messages).start()

c1.send_message("hi buddy")
time.sleep(2)
c2.send_message("hi hooman")
time.sleep(2)
c1.send_message("how you doing")
time.sleep(2)
c2.send_message("nothing much bro")
time.sleep(2)

c1.disconnect()
time.sleep(2)
c2.disconnect()

