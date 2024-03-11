from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser, OrderTable


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderTable
        fields = ["name", "image_url", "quantity", "measurement", "teachers_comments"]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

class SmOrderEdit(forms.ModelForm):
    class Meta:
        model = OrderTable
        fields = ["price", "sm_comments", "status", "date_of_reciept"]

    def __init__(self, *args, **kwargs):
        super(SmOrderEdit, self).__init__(*args, **kwargs)


class StOrderEdit(forms.ModelForm):
    class Meta:
        model = OrderTable
        fields = ["st_comments", "in_stock", "teacher_recieved", "delivered_quantity", "status"]

    def __init__(self, *args, **kwargs):
        super(StOrderEdit, self).__init__(*args, **kwargs)
