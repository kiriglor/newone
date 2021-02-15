from django.shortcuts import get_object_or_404, render


def mainpage(request):
    return render(request, "homepage/main.html")
