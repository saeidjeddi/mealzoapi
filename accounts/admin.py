from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
from .forms import UserChangeForm, UserCreationForm


admin.site.site_header = 'Mealzo panel admin'
admin.site.site_title = 'Mealzo'
admin.site.index_title = 'Mealzo panel'


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["username", "full_name", "email", "is_active", "is_admin", "is_superuser", "is_developer", "is_management", "is_onboarding", "is_support", "is_marketing", ]
    list_filter = ["is_active", "is_admin", "is_superuser", "is_developer", "is_management", "is_onboarding", "is_support", "is_marketing"]
    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Personal info", {"fields": ["email","full_name"]}),
        ("Permissions", {"fields": ["is_active", "is_admin", "is_superuser", "is_developer", "is_management", "is_onboarding", "is_support", "is_marketing"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username","full_name", "email", "password1", "password2",  "is_active", "is_admin", "is_superuser", "is_developer", "is_management", "is_onboarding", "is_support", "is_marketing"],
            },
        ),
    ]
    search_fields = ["email", 'username', 'full_name']
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
