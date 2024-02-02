from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):

    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    phonenumber = models.CharField(max_length=200, null=True, blank=True)
    social_media_profiles = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)



    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    

