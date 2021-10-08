from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        """
        Creates and saves a User with the given phone number and password.
        """

        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(
            phone_number=self.normalize_email(phone_number),
            username=self.normalize_email(phone_number),
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone_number, email, password=None):
        """
        Creates and saves a superuser with the given phone number and password.
        """

        user = self.create_user(phone_number, password=password)
        user.email=email
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractUser):
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email']

    email = models.EmailField(
        verbose_name="Email address", max_length=255, unique=True, blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return self.username
