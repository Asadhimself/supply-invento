from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import CustomUser, OrderTable
from .forms import OrderForm, SmOrderEdit, StOrderEdit


def make_pagination(request, obj):
    p = Paginator(obj, 10)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    return page_obj


def is_editable()-> bool:
    pass

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
    if request.user.is_staff:
        admin_url = reverse("admin:index")
        return redirect(admin_url)
    if request.user.role == "Teacher":
        table = OrderTable.objects.filter(user=request.user, is_archive=False)
        for order in table:
            order.status = order.status.split()[0]
        table = list(enumerate(table, start=1))
        table = make_pagination(request, table)
        return render(request, "supply/teachers_home.html", {"table": table})
    elif request.user.role == "Supplier" or request.user.role == "Storekeeper":
        classes = ["EYPYP", "PYP", "MYP", "DP"]
        return render(request, "supply/manager_home.html", {"classes": classes})
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
        return HttpResponseForbidden()
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
    if request.user.role not in ["Supplier", "Storekeeper"]:
        return HttpResponse("Access is forbidden")
    if pk not in ["EYPYP", "PYP", "MYP", "DP"]:
        return Http404()
    teachers = CustomUser.objects.filter(user_class=pk)
    return render(
        request, "supply/section_teachers.html", {"teachers": teachers, "class": pk}
    )


@login_required(login_url="/login")
def manage_teachers_table(request, user_id):
    if request.user.role not in ["Supplier", "Storekeeper"]:
        return HttpResponse("Access is forbidden")
    min_date = request.GET.get('min_date')
    max_date = request.GET.get('max_date')
    orders = OrderTable.objects.filter(user=user_id, is_archive=False)
    if min_date or max_date:
        date_filter = Q()
        if min_date:
            date_filter |= Q(order_date__gte=min_date) | Q(date_of_reciept__gte=min_date)

        if max_date:
            date_filter |= Q(order_date__lte=max_date) | Q(date_of_reciept__lte=max_date)
        print(len(orders))
        orders = orders.filter(date_filter)
        print(len(orders))
    for order in orders:
        order.status = order.status.split()[0]
    teacher = CustomUser.objects.get(id=user_id)
    orders = make_pagination(request, orders)
    return render(
        request,
        "supply/manage_teachers_table.html",
        {"orders": orders, "teacher": teacher},
    )


@login_required(login_url="/login")
def sm_edit_view(request, order_id):
    if request.user.role != "Supplier":
        return HttpResponse("Access is forbidden")
    order = get_object_or_404(OrderTable, pk=order_id)
    if request.method == "POST":
        form = SmOrderEdit(request.POST, instance=order)
        form.save()
        user_id = order.user.id
        return redirect("manage_table", user_id)
    else:
        form = SmOrderEdit(instance=order)
    return render(request, "supply/sm_edit.html", {"form": form, "order": order})


@login_required
def st_edit_view(request, order_id):
    if request.user.role != "Storekeeper":
        return HttpResponse("Access is forbidden")
    order = get_object_or_404(OrderTable, pk=order_id)
    if request.method == "POST":
        form = StOrderEdit(request.POST, instance=order)
        form.save()
        user_id = order.user.id
        return redirect("manage_table", user_id)
    else:
        form = StOrderEdit(instance=order)
    return render(request, "supply/st_edit.html", {"form": form, "order": order})


@login_required(login_url="/login")
def manage_delete_order_view(request, order_id):
    order = get_object_or_404(OrderTable, pk=order_id)
    order_user_id = order.user.id
    if request.user.role in ["Supplier", "Storekeeper"]:
        if request.method == "POST" or request.method == "GET":
            order.delete()
            return redirect("manage_table", order_user_id)


@login_required(login_url="/login")
def teacher_archive_view(request):
    table = OrderTable.objects.filter(user=request.user, is_archive=True)
    return render(request, "supply/archive_teacher.html", {"table": table})


@login_required(login_url="/login")
def manage_archive_view(request, user_id):
    if request.user.role not in ["Supplier", "Storekeeper"]:
        return HttpResponse("Access is forbidden")
    orders = OrderTable.objects.filter(user=user_id, is_archive=True)
    for order in orders:
        order.status = order.status.split()[0]
    teacher = CustomUser.objects.get(id=user_id)
    orders = make_pagination(request, orders)
    return render(
        request,
        "supply/archive_manage.html",
        {"orders": orders, "teacher": teacher},
    )


def custom_403(request, exception):
    return render(request, "errors/403.html", status=403)
