from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import OrderTable, CustomUser
from .forms import OrderForm


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

def base_view(request):
    return render(request, 'supply/base.html')


@login_required(login_url="/login")
def home_view(request):
    # if request.user.is_staff:
    #     admin_url = reverse("admin:index")
    #     return redirect(admin_url)
    if request.user.role == "Teacher":
        table = OrderTable.objects.filter(customer=request.user)
        table = list(enumerate(table, start=1))
        email = request.user.email
        return render(request, "supply/teachers_home.html", {"table": table, "email": email})
    return render(request, "supply/home.html")

@login_required(login_url='/login')
def add_order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('home')
    else:
        form = OrderForm()

    return render(request, "supply/add_order.html", {'form': form})
