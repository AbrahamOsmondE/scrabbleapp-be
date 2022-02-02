from django.db import transaction
from django.core.management.utils import get_random_secret_key

from datetime import datetime

from users.models import User


def user_create(email, is_seller=False, password=None, **extra_fields):
    extra_fields = {
        'is_staff': False,
        'is_superuser': False,
        'is_seller': is_seller,
        **extra_fields
    }

    user = User(email=email, **extra_fields)

    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()

    user.full_clean()
    user.save()

    return user


def user_create_superuser(email, password=None, **extra_fields) -> User:
    extra_fields = {
        **extra_fields,
        'is_staff': True,
        'is_seller': True,
        'is_buyer': True,
        'is_superuser': True
    }

    user = user_create(email=email, password=password, **extra_fields)

    return user


def user_record_login(*, user: User):
    user.last_login = datetime.now()
    user.save()

    return user


@transaction.atomic
def user_get_or_create(*, email: str, google_id: str, **extra_data):
    user = User.objects.filter(email=email).first()

    if user:
        return user, False

    return user_create(email=email, google_id=google_id, **extra_data), True
