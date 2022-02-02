from django.test import TestCase
from .services import user_create_superuser

user_create_superuser(
    email='abraham.osmond@gmail.com',
    password='MistamaN2506!'
)
# Create your tests here.
