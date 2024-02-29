from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'supply/login.html', {'error_message': 'Invalid email/password'})    

    return render(request, 'supply/login.html')

@login_required(login_url='/login')
def home_view(request):
    return HttpResponse("Hello world")