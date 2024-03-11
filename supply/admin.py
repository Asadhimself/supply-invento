from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, OrderTable
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("get_user_info", "user_class", "is_staff", "is_active", "role")
    list_filter = ("is_staff", "is_active", "role", "user_class")
    fieldsets = (
        (None, {"fields": ("first_name", "last_name","email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("User info", {"fields": ("role", "user_class")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
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
    search_fields = ("email", "user_class", "first_name", "last_name")
    ordering = ("email",)
    def get_user_info(self, obj):
        if obj.user_class:
            return f"{obj.first_name} {obj.last_name}"
        else:
            return f"{obj.first_name} {obj.last_name} ({obj.role})"
        

class OrderTableAdmin(admin.ModelAdmin):
    readonly_fields = ('order_date', 'date_of_reciept')
    list_display = ('id', 'name', 'user', 'get_photo', 'status',)
    list_filter = ('status', )
    search_fields = ('id', 'user__first_name', 'user__last_name', 'user__email', 'name')
    def get_photo(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" width=50px>')
        return '-'

    get_photo.short_description = 'Image'


admin.site.unregister(Group)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OrderTable, OrderTableAdmin)

#site visuals
admin.site.site_header = "Supply Administration"
admin.site.site_title = "Supply Invento"
admin.site.index_title = "Supply Invento"
