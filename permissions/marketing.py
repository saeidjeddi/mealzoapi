import requests
from rest_framework.permissions import BasePermission


class Member(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if  request.user.active and request.user.googleBusinessMap or request.user.superuser:
                return True
            else:
                return False
        else:
            return False


class MemberAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.googleBusinessMap and request.user.gbDashboardEdit and request.user.active or request.user.superuser:
                return True
            else:
                return False
        else:
            return False


class GbDashboardCountMap(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if  request.user.active and request.user.googleBusinessMap and request.user.gbMapCount or request.user.superuser:
                return True
            else:
                return False
        else:
            return False


class GbDashboardCountWeb(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if  request.user.active and request.user.googleBusinessMap and request.user.gbWebCount or request.user.superuser:
                return True
            else:
                return False
        else:
            return False



class GbDashboardsercheCount(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if  request.user.active and request.user.googleBusinessMap and request.user.gbDSerchecount or request.user.superuser:
                return True
            else:
                return False
        else:
            return False



class GbDashboardKeywords(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if  request.user.active and request.user.googleBusinessMap and request.user.gbKeywords or request.user.superuser:
                return True
            else:
                return False
        else:
            return False
