from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
from django.utils.timezone import now


class User(AbstractBaseUser):
    """
    در این کلاس کاربران تعریف و نقش و دسترسی ها تعریف شذه .
    """

    department_CHOICES = [
        ('SuperUser', 'SuperUser'),
        ('Developer', 'Developer'),
        ('Marketing', 'Marketing'),
        ('Support', 'Support'),
        ('Onboarding', 'Onboarding'),
        ('Management', 'Management'),
        ('Menu', 'Menu'),
        ('UX/UI', 'UX/UI'),
    ]
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True, choices=department_CHOICES)
    active = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    # ---------
    gbKeywords = models.BooleanField(default=False)
    googleBusinessMap = models.BooleanField(default=False)
    gbDashboardMap = models.BooleanField(default=False)
    googleBusinessPanel = models.BooleanField(default=False)
    gbMapCount = models.BooleanField(default=False)
    gbWebCount = models.BooleanField(default=False)
    gbDSerchecount = models.BooleanField(default=False)
    gbDashboardEdit = models.BooleanField(default=False)
    # ---------
    devices = models.BooleanField(default=False)
    companies = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ----------
    isLimited = models.BooleanField(default=False)
    timeRequestRemaining = models.DateTimeField(default=now)
    refreshTimeRequest = models.IntegerField(default=24, help_text="After the time is up, this time is added * in hours.")
    numberOfRequestRemaining = models.IntegerField(default=0)
    refreshNumberRequest = models.IntegerField(default=20, help_text="After the number is up, this number is added * in hours.")

    # ----------

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin

