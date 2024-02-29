from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "supply/login.html",
                {"error_message": "Invalid email/password"},
            )

    return render(request, "supply/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="/login")
def home_view(request):
    return render(request, "supply/home.html")
