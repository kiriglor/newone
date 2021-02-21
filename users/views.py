from django.shortcuts import render, redirect
from .form import UserForm
from users.models import User


def users_profile_view(request, nickname):
    print(User.objects.get(nickname=nickname))
    current_user = User.objects.get(nickname=nickname)
    print(current_user)
    return render(request, "users/user_profile.html", {"user": current_user})


def authorization_view(request):
    form_obj = UserForm(request.POST or None)
    return render(request, "users/auth.html", {"form": form_obj, "nickname": request.POST.get(form_obj.cleaned_data['nickname'])})
