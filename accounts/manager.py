from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, full_name=None,department=None,
                    active=None, admin=None, superuser=None, allowedChange=None,
                    getInfo=None, googleBusiness=None, device=None, company=None, password=None, ):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
            department=department,
            active=active,
            admin=admin,
            superuser=superuser,
            allowedChange=allowedChange,
            getInfo=getInfo,
            googleBusiness=googleBusiness,
            device=device,
            company=company

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
        user.admin = True
        user.active = True
        user.superuser = True
        user.save(using=self._db)
        return user
