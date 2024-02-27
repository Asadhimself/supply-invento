from django.contrib import admin
from django.contrib.auth.models import Group
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, OrderTable
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active", "role")
    list_filter = ("email", "is_staff", "is_active", "role", "user_class")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("User info", {"fields": ("role", "user_class")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "role",
                    "user_class",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.unregister(Group)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OrderTable)

#site visuals
admin.site.site_header = "Supply Administration"
admin.site.site_title = "Supply Invento"
admin.site.index_title = "Supply Invento"
