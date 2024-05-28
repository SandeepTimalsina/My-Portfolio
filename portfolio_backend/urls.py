from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name = "home"),
    path('home/send-email',views.send_email , name ="send_email")
]