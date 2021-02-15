from django.shortcuts import render


def users_profile_view(request, user):
    return render(request, "users/users_profile_view", {"user": user})


def authorization_view(request):
    return render(request, "users/auth.html", {})
