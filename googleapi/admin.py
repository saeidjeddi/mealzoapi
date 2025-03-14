from django.contrib import admin
from .models import PhoneLoge, TitleLoge, WebsiteLoge, OpenHoursLoge



class PhoneLogeAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'shop', 'location')
    search_fields = ('username', 'email', 'shop', 'chenge', 'location')
    list_filter = ('chengeTime',)
    list_per_page = 15

    def get_readonly_fields(self, request, obj=None):
        return ['username', 'email', 'shop', 'chenge', 'location','chengeTime']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass




admin.site.register(PhoneLoge, PhoneLogeAdmin)


class TitleLogeAdmin(admin.ModelAdmin):
    list_display = ('username','email','website','location')
    search_fields = ('username','email','website', 'chenge', 'location')
    list_filter = ('chengeTime',)
    list_per_page = 15

    def get_readonly_fields(self, request, obj=None):
        return ['username','email','website', 'chenge', 'location','chengeTime']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass




admin.site.register(TitleLoge,TitleLogeAdmin)

class WebsiteLogeAdmin(admin.ModelAdmin):
    list_display = ('username','email','shop','location')
    search_fields = ('username','email','shop', 'chenge', 'location')
    list_filter = ('chengeTime',)
    list_per_page = 15


    def get_readonly_fields(self, request, obj=None):
        return ['username','email','shop', 'chenge', 'location','chengeTime']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass



admin.site.register(WebsiteLoge, WebsiteLogeAdmin)

class OpenHoursLogeAdmin(admin.ModelAdmin):
    list_display = ('username','email','shop','chengeTime','chenge','location')
    search_fields = ('username','email','shop', 'chenge', 'location')
    list_filter = ('chengeTime',)
    list_per_page = 15

    def get_readonly_fields(self, request, obj=None):
        return ['username','email','shop','chengeTime','chenge','location']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass



admin.site.register(OpenHoursLoge, OpenHoursLogeAdmin)

