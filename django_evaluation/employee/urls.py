from django.urls import path
from .views import register,registration,display,starts

urlpatterns = [
    path("",register, name="register"),
    path("register/",registration, name="registration"),
    path("<int:eid>/",display, name="display"),
    path("starts/",starts,name="starts")
]