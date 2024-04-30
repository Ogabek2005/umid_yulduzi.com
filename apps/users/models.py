from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from django.utils import timezone
import random
from apps.common.models import BaseModel

TIME = 1
USER, ADMIN , DONATER = 'user', 'admin', 'donater'
from django.core import validators
from django.utils.deconstruct import deconstructible

@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r"^\+998\d{9}$"
    message = "To'g'ri keladigan telefon raqam kiriting"
    flags = 0


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, password, **extra_fields)

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)


class UserConfirmation(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='confirmation',
    )
    code = models.CharField(max_length=4)
    expire_datetime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # if self.code:
        #     self.expire_datetime = timezone.now() + datetime.timedelta(minutes=TIME)
        super(UserConfirmation, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return f"{self.code} {self.user.phone_number}"

class User(AbstractUser):

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    username = None

    phone_validator = PhoneValidator()
    TYPE = (
        (ADMIN, "Admin"),
        (USER, "User"),
        (DONATER, "Donater")
    )
    auth_status = models.BooleanField(default=False)
    type = models.CharField(max_length=100, choices=TYPE, default=DONATER)
    phone_number = models.CharField(
        max_length = 13,
        verbose_name='Phone number',
        validators = [phone_validator],  
        unique = True     
    )
    birth_date = models.DateField(verbose_name='Birth date', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.id} - {self.phone_number}"
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def get_code(self):
        confirmation = UserConfirmation.objects.filter(user=self).first()
        code = ''.join([str(random.randint(0, 1000))[-1] for _ in range(4)])
        if confirmation:
            confirmation.code = code
            confirmation.save(update_fields=['code'])
        else:
            UserConfirmation.objects.create(user=self, code=code)
        return code

        

class NeedHelp(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    dead_line = models.DateTimeField()
    amount_money = models.DecimalField(max_digits=20, decimal_places=2)
    file = models.FileField(upload_to='file/', null=True, blank=True)
    locations = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.phone_number