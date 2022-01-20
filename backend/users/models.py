from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.management.utils import get_random_secret_key

# Create your models here.


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, db_index=True)
    secret_key = models.CharField(
        max_length=255, default=get_random_secret_key)
    google_id = models.CharField(
        max_length=50, unique=True, db_index=True, blank=True)
    is_buyer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    @property
    def name(self):
        if not self.last_name:
            return self.first_name.capitalize()

        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
