from django.db import models

from django.contrib.auth.models import AbstractUser


NULLABLE = {"null": True, "blank": True}



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=35, verbose_name="номер телефона", **NULLABLE)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
