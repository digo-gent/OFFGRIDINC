from django.contrib import admin
from .models import Account
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import AccountChangeForm, AccountCreationForm

# Register your models here.

class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    
    list_display=("email","username","is_admin","is_staff","last_login","joined_at")
    exclude_fields=("last_joined","joined_at")
    readonly_fields = ("joined_at", "last_login")
    
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("is_active", "is_admin", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "joined_at")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_active", "is_admin", "is_superuser"),
        }),
    )
    
    filter_horizontal=()
    list_filter=()

admin.site.register(Account, AccountAdmin),