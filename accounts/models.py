from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserModelManager(BaseUserManager):

    def create_user(self,
                    email=None,
                    phone=None,
                    password=None,
                    **extra_fields):
        if not email and not phone:
            raise ValueError(
                _("Renseigner votre email ou numero de telephone"))

        if email:
            email = self.normalize_email(email=email)
            user = self.model(email=email, **extra_fields)
        else:
            user = self.model(phone=phone, **extra_fields)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    username = None
    first_name = None
    last_name = None

    objects = CustomUserModelManager()
