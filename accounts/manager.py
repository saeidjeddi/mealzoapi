from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name=None, password=None, is_active=None, is_admin=None,
                    is_superuser=None, is_developer=None, is_marketing=None, is_support=None,
                    is_onboarding=None, is_management=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError("Users must have an username ")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
            is_active=is_active,
            is_admin=is_admin,
            is_superuser=is_superuser,
            is_developer=is_developer,
            is_management=is_management,
            is_onboarding=is_onboarding,
            is_support=is_support,
            is_marketing=is_marketing,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.is_developer = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
