from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['telephone', 'password']
    EMAIL_FIELD = ['email'] 
    
    
