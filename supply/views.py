import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from .models import CustomUser, OrderTable
from .forms import OrderForm, SmOrderEdit, StOrderEdit


def make_pagination(request, obj):
    p = Paginator(obj, 10)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    return page_obj


def is_editable(user_class) -> bool:
    today = timezone.now().date()
    if user_class == "EYPYP":
        start_date = today.replace(day=1)
        end_date = today.replace(day=15)
    else:
        start_date = today.replace(day=16)
        end_date = today.replace(day=timezone.now().day)
    return start_date <= today <= end_date


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

    if not is_editable(request.user.user_class):
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
        return HttpResponseForbidden()
    if not is_editable(request.user.user_class):
        return HttpResponseForbidden()
    if request.method == "POST" or request.method == "GET":
        order.delete()
        return redirect("home")


@login_required(login_url="/login")
def profile_view(request, user_id):
    if request.user.id == user_id:
        user = CustomUser.objects.get(id=user_id)
        return render(request, "supply/profile.html", {"user": user})
    else:
        return HttpResponseForbidden()


@login_required(login_url="/login")
def section_view(request, pk):
    if request.user.role not in ["Supplier", "Storekeeper"]:
        return HttpResponseForbidden()
    if pk not in ["EYPYP", "PYP", "MYP", "DP"]:
        return Http404()
    teachers = CustomUser.objects.filter(user_class=pk)
    return render(
        request, "supply/section_teachers.html", {"teachers": teachers, "class": pk}
    )


@login_required(login_url="/login")
def manage_teachers_table(request, user_id):
    if request.user.role not in ["Supplier", "Storekeeper"]:
        return HttpResponseForbidden()
    min_date = request.GET.get("min_date")
    max_date = request.GET.get("max_date")
    date_filter = Q()
    if min_date:
        min_date = datetime.datetime.strptime(min_date, "%Y-%m-%d").replace(
            tzinfo=datetime.timezone.utc
        )
        date_filter |= Q(order_date__gte=min_date)
    if max_date:
        max_date = datetime.datetime.strptime(max_date, "%Y-%m-%d").replace(
            tzinfo=datetime.timezone.utc
        )
        date_filter |= Q(order_date__lte=max_date)
    orders = OrderTable.objects.filter(user=user_id, is_archive=False)
    orders = orders.filter(date_filter)
    for order in orders:
        order.status = order.status.split()[0]
    teacher = CustomUser.objects.get(id=user_id)
    if orders:
        orders = make_pagination(request, orders)
    context = {"orders": orders, "teacher": teacher}
    if min_date:
        context.setdefault("min_date", request.GET.get("min_date"))
    if max_date:
        context.setdefault("max_date", request.GET.get("max_date"))
    return render(
        request,
        "supply/manage_teachers_table.html",
        context,
    )


@login_required(login_url="/login")
def sm_edit_view(request, order_id):
    if request.user.role != "Supplier":
        return HttpResponseForbidden()
    order = get_object_or_404(OrderTable, pk=order_id)
    if request.method == "POST":
        form = SmOrderEdit(request.POST, instance=order)
        if form.is_valid():
            new_status = form.cleaned_data["status"]
            if new_status == "Fully recieved":
                order.date_of_reciept = timezone.now()
        form.save()
        user_id = order.user.id
        return redirect("manage_table", user_id)
    else:
        form = SmOrderEdit(instance=order)
    return render(request, "supply/sm_edit.html", {"form": form, "order": order})


@login_required
def st_edit_view(request, order_id):
    if request.user.role != "Storekeeper":
        return HttpResponseForbidden()
    order = get_object_or_404(OrderTable, pk=order_id)
    if request.method == "POST":
        form = StOrderEdit(request.POST, instance=order)
        if form.is_valid():
            new_status = form.cleaned_data["status"]
            if new_status == "Fully recieved":
                order.date_of_reciept = timezone.now()
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
    for order in table:
        order.status = order.status.split()[0]
    table = list(enumerate(table, start=1))
    table = make_pagination(request, table)
    return render(request, "supply/archive_teacher.html", {"table": table})


@login_required(login_url="/login")
def manage_archive_view(request, user_id):
    if request.user.role not in ["Supplier", "Storekeeper"]:
        return HttpResponseForbidden()
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


@login_required(login_url="/login")
def archive_order(request, order_id):
    if request.user.role in ["Supplier", "Storekeeper"]:
        order = get_object_or_404(OrderTable, id=order_id)
        order_user_id = order.user.id
        order.is_archive = True
        order.save()
        return redirect("manage_table", order_user_id)
    elif request.user.role == "Teacher" and is_editable(request.user.user_class):
        order = get_object_or_404(OrderTable, id=order_id)
        order.is_archive = True
        order.save()
        return redirect("home")
    else:
        raise HttpResponseForbidden()


@login_required(login_url="/login")
def unarchive_order(request, order_id):
    if request.user.role in ["Supplier", "Storekeeper"]:
        order = get_object_or_404(OrderTable, id=order_id)
        order_user_id = order.user.id
        order.is_archive = False
        order.save()
        return redirect("manage_archive", order_user_id)
    elif request.user.role == "Teacher" and is_editable(request.user.user_class):
        order = get_object_or_404(OrderTable, id=order_id)
        order.is_archive = False
        order.save()
        return redirect("teacher_archive")
    else:
        raise HttpResponseForbidden()


@login_required(login_url="/login")
def search_view(request, user_id):
    if request.user.role in ["Supplier", "Storekeeper"]:
        teacher = CustomUser.objects.get(id=user_id)
        search = request.GET.get("search", "")
        result = OrderTable.objects.filter(
            Q(name__icontains=search)
            | Q(teachers_comments__icontains=search)
            | Q(sm_comments__icontains=search)
            | Q(st_comments__icontains=search),
            user_id=user_id,
            is_archive=False
        )
        orders = make_pagination(request, result)
        return render(
            request,
            "supply/manage_teachers_table.html",
            {"orders": orders, "teacher": teacher, "search": search},
        )
    else:
        raise HttpResponseForbidden()

@login_required(login_url="/login")
def search_archive_view(request, user_id):
    if request.user.role in ["Supplier", "Storekeeper"]:
        teacher = CustomUser.objects.get(id=user_id)
        search = request.GET.get("search", "")
        result = OrderTable.objects.filter(
            Q(name__icontains=search)
            | Q(teachers_comments__icontains=search)
            | Q(sm_comments__icontains=search)
            | Q(st_comments__icontains=search),
            user_id=user_id,
            is_archive=True
        )
        orders = make_pagination(request, result)
        return render(
            request,
            "supply/archive_manage.html",
            {"orders": orders, "teacher": teacher, "search": search},
        )
    else:
        raise HttpResponseForbidden()
