from django.shortcuts import render, get_object_or_404
from .models import Command


def commands_view(request):
    command_list = Command.objects.order_by("command_name")
    commands = {
        "command_list": command_list
    }
    return render(request, "commands/command_list.html", commands)


def command_view(request, command_name_url):
    command_profile_object = Command.objects.get(command_name=command_name_url)
    profile = {
        "command_profile_object_name":command_profile_object.command_name,
        "command_profile_object_members":command_profile_object.group_members.all(),
    }
    return render(request, "commands/command_profile.html", profile)