from django.urls import path
from .views import index, Login, logout, createUser

urlpatterns = [
    path('', index, name="index"),
    path('login/', Login, name="login"),
    path('logout/', logout, name="logout"),
    path('create/', createUser, name="createUser"),
]
