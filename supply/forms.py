from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser, OrderTable


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderTable
        fields = ['name', 'image_url', 'quantity', 'measurement', 'teachers_comments']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)