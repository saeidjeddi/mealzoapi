from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from urllib3 import request

from accounts.models import User
from .forms import UserChangeForm, UserCreationForm


admin.site.site_header = 'Mealzo R&D panel admin'
admin.site.site_title = 'Mealzo R&D'
admin.site.index_title = 'Mealzo R&D panel'

class UserAdmin(BaseUserAdmin):
    """
در این کلاس که از BaseUserAdmin  ارث بری میکنه
پنل ادمین رو اختصاصی کردم . که بگونه که پرمیژن ها دسته بندی شده .
    """
    form = UserChangeForm
    add_form = UserCreationForm
    list_per_page = 10
    list_display = ["username", "id", "full_name", "email",'active', "devices", "companies", "googleBusinessMap", "googleBusinessPanel"]
    list_filter = ['active', "devices", "companies", "googleBusinessMap"]
    list_editable = ['active']
    fieldsets = [
        (None, {"fields": ["username", "password", "department", "email", "full_name"]}),
        ("Personal User", {"fields": ["active","admin", "superuser", "timeRequestRemaining", "numberOfRequestRemaining", "isLimited", "refreshTimeRequest", "refreshNumberRequest"]}),
        ("Permissions googleBusiness", {"fields": ["googleBusinessMap","gbDashboardMap", "gbKeywords","googleBusinessPanel", "gbDashboardEdit","gbMapCount", "gbWebCount", "gbDSerchecount"]}),
        ("Permissions device", {"fields": ["devices",]}),
        ("Permissions companies", {"fields": ["companies",]}),
    ]



    add_fieldsets = [
        ('User info',{
                "classes": ["wide"],
                "fields": ["username", "full_name", "email", "department", "password1", "password2", "active","admin","superuser"],
            },),
            
        ("Permissions googleBusiness", {"fields": ["googleBusinessMap","gbDashboardMap", "gbKeywords","googleBusinessPanel", "gbDashboardEdit","gbMapCount", "gbWebCount", "gbDSerchecount"]}),
        ("Permissions device", {"fields": ["devices",]}),
        ("Permissions companies", {"fields": ["companies",]}),
    ]

    search_fields = ["email", "username", "full_name", 'id']
    ordering = ["email"]
    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if not request.user.superuser:
            return ['superuser', 'username', 'email', 'full_name', 'password', 'department']
        return []


    def has_add_permission(self, request):
        return request.user.superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.superuser





admin.site.register(User, UserAdmin)
admin.site.unregister(Group)