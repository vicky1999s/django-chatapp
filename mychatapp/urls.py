from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("test", views.send_message, name="send_message"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout")
]
