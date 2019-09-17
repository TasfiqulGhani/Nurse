from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import UserManager, Group as RoleModel, PermissionsMixin
# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser

from django.utils import timezone


class Role(RoleModel):
    class Meta:
        proxy = True


class UserPermissionsMixin(PermissionsMixin):
    groups = None  # remove this field from super class
    user_permissions = None  # remove this field from super class

    role = models.ForeignKey(Role, null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class SimpleUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.is_active = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=20, default='123456')
    dob = models.DateField(null=True, blank=True)
    code = models.CharField(max_length=10, default='')
    fb_token = models.CharField(max_length=10, default='')
    fire_token = models.CharField(max_length=10, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []


class Employee(AbstractBaseUser):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=20, default='123456')
    dob = models.DateField(null=True, blank=True)
    code = models.CharField(max_length=10, default='')
    fb_token = models.CharField(max_length=10, default='')
    fire_token = models.CharField(max_length=10, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []


class Customer(AbstractBaseUser):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=20, default='123456')
    dob = models.DateField(null=True, blank=True)
    code = models.CharField(max_length=10, default='')
    fb_token = models.CharField(max_length=10, default='')
    fire_token = models.CharField(max_length=10, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
