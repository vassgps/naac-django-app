#ProApp/Urls.py
from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views
from .views import *

app_name = 'proApp'

urlpatterns = [
    path('', index, name="index"),
    path('register/', register,name="register"),
    # path('accounts/login/', getLogin.as_view(), name="login"),
    path('login/',login, name="login"),
    # path('logout/', logout, name="logout"),
    # path('contact/', contact, name='Contact'),
    # path('password/', invaildUrl, name='ivaildurl'),
    # path('regdone', regDone , name='regdone'),
    # path('staff', staff , name='staff'),
]
