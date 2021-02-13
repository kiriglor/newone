from django.urls import include,path
from . import views

urlpatterns = [
    path("", views.mainpage, name="main"),
    ]