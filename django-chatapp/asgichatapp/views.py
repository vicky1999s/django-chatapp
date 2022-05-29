from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    print("index page")
    print(request)
    if request.method=="GET":
        return render(request, "asgichatapp/index.html")
    username = request.POST["username"]
    print(username)
    return render(request, "asgichatapp/room.html", {"username":username})

def room(request):
    print("room func")
    return render(request, "asgichatapp/room.html", {})
