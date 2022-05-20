import time
from urllib import request as testing
from django.http import HttpResponse
from django.shortcuts import redirect, render
from threading import Thread


#from client import Client
from client import Client

client = None
messages = []
# Create your views here.
NAME_KEY = 'name'
def home(request):
    if NAME_KEY not in request.session:
        return redirect('login')
    
    return render(request, 'mychatapp/index.html')
    

def send_message(request):
    global client
    msg = request.POST['msg']
    print(messages)
    if client!=None:
        client.send_message(msg)
        
    return HttpResponse("success")

def get_msg(request, msg):
    print(msg)

def login(request):
    global client
    if client:
        client.disconnect()
    if request.method == "POST":
        name = request.POST["name"]
        request.session[NAME_KEY] = name
        client = Client(name)
        Thread(target=update_messages).start()
        client.send_message(name)
        return redirect("home")
    return render(request, "mychatapp/login.html")

def logout(request):
    try:
        del request.session[NAME_KEY]
        # print("inside logout ")
        # print(client)
        # client.disconnect()
    except KeyError:
        pass
    return redirect('login')

def update_messages():
    global client
    print("INSIDE UPDATE MESSAGES")
    global messages
    messages = []
    run = True
    while run:  
        time.sleep(1)
        if not client: continue
        new_msgs = client.get_messages()
        messages.extend(new_msgs)
        for msg in new_msgs:
            get_msg(testing, msg)
            print("up====>"+msg)
            if msg=="quit":
                run = False
                break
    

