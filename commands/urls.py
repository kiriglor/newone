from django.urls import include,path

from . import views


urlpatterns = [
    path("", views.commands_view, name="commands"),
    path("<str:command_name_url>/", views.command_view, name="command")
]