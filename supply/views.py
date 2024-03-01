from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import CustomUser, OrderTable
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
                {"error_message": "Invalid email / password"},
            )

    return render(request, "supply/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="/login")
def home_view(request):
    # if request.user.is_staff:
    #     admin_url = reverse("admin:index")
    #     return redirect(admin_url)
    if request.user.role == "Teacher":
        table = OrderTable.objects.filter(user=request.user)
        for order in table:
            order.status = order.status.split()[0]
        table = list(enumerate(table, start=1))
        return render(request, "supply/teachers_home.html", {"table": table})
    elif request.user.role == "Supplier":
        classes = ["EYPYP", "PYP", "MYP", "DP"]
        return render(request, "supply/suppliers_home.html", {"classes": classes})
    return render(request, "supply/home.html")


@login_required(login_url="/login")
def add_order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
        return redirect("home")
    else:
        form = OrderForm()

    return render(request, "supply/add_order.html", {"form": form})


@login_required(login_url="/login")
def edit_order_view(request, order_id):
    order = get_object_or_404(OrderTable, pk=order_id)
    if order.user != request.user:
        return render(HttpResponse("Acces is forbidden"))
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = OrderForm(instance=order)

    return render(request, "supply/edit_order.html", {"form": form, "order": order})


@login_required(login_url="/login")
def delete_order_view(request, order_id):
    order = get_object_or_404(OrderTable, pk=order_id)
    if request.user != order.user:
        return render(HttpResponse("Access is forbidden"))
    if request.method == "POST" or request.method == "GET":
        order.delete()
        return redirect("home")


@login_required(login_url="/login")
def profile_view(request, user_id):
    if request.user.id == user_id:
        user = CustomUser.objects.get(id=user_id)
        return render(request, "supply/profile.html", {"user": user})
    else:
        return HttpResponse("Access is forbidden")


@login_required(login_url="/login")
def section_view(request, pk):
    if pk not in ["EYPYP", "PYP", "MYP", "DP"]:
        return Http404()
    teachers = CustomUser.objects.filter(user_class=pk)
    return render(
        request, "supply/section_teachers.html", {"teachers": teachers, "class": pk}
    )


@login_required(login_url="/login")
def sm_teachers_table(request, user_id):
    orders = OrderTable.objects.filter(user=user_id)
    for order in orders:
        order.status = order.status.split()[0]
    teacher = CustomUser.objects.get(id=user_id)
    return render(
        request, "supply/sm_teachers_table.html", {"orders": orders, "teacher": teacher}
    )
