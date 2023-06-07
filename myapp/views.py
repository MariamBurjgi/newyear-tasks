from django.shortcuts import render
from django.http import HttpResponse


def greet(request, name):
    return render(request, "myapp/index.html", {
        "name": name.capitalize()
    })

