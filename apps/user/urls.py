#Users/Urls
from django.urls import path
from .views import *


app_name = "user"

urlpatterns = [
    # path("verify-email/<str:uid>", VerifyEmail.as_view()),
    # path("resend-email", ResendVerifyMail.as_view()),
    path("index", home, name="index"),
    path("home", home, name="home"),
    path("login", GetLogin.as_view() , name="login"),
    path("logout", logout, name="logout"),
    path("criterion/<str:cid>", Criterion.as_view(), name="criterion"),
    path('register', signup, name="register"),
    path('update', UpdateUser.as_view(), name="update"),
    path('change-password', ChangePassword.as_view(), name="change-password"),
    # path('loadmenu', LoadMenu.as_view(), name="loadmenu"),
    path('club-management/<int:id>', ClubManagement.as_view(), name="club-management"),
  ]

