from django.urls import path
from . import views

urlpatterns = [
    path("<str:nickname>", views.users_profile_view, name="profile_view"),
    path("", views.authorization_view, name="auth")
]