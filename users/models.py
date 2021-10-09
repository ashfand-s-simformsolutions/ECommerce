from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password=None):
        """
        Creates and saves a User with the given phone number and password.
        """

        user = self.model(phone_number=phone_number, username=phone_number, email=email)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone_number, email, password=None):
        """
        Creates and saves a superuser with the given phone number and password.
        """

        user = self.model(
            phone_number=phone_number,
            email=email,
            username=phone_number,
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()

        return user


def get_profile_image_filepath(self, filename):
	return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
	return "default_image"


class User(AbstractUser):
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email"]

    phone_regex = RegexValidator(
        regex="^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$", message="Enter valid Indian number"
    )

    email = models.EmailField(
        verbose_name="Email address", max_length=255, unique=True, blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(
        max_length=20, unique=True, validators=[phone_regex]
    )
    username = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_superuser
