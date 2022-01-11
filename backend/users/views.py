from django.shortcuts import render
import requests

from django.conf import settings
from .serializers import UserSerializer
from .services import user_get_or_create

from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from rest_framework.response import Response

GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'


def google_validate_id_token(*, id_token: str) -> bool:
    response = requests.get(
        GOOGLE_ID_TOKEN_INFO_URL,
        params={'id_token': id_token}
    )
    if not response.ok:
        raise ValidationError('id_token is invalid.')

    audience = response.json()['aud']

    if audience != settings.GOOGLE_OAUTH2_CLIENT_ID:
        raise ValidationError('Invalid audience.')
    return True
# Create your views here.


@api_view(['POST'])
def login(request, *args, **kwargs):
    id_token = request.headers.get('Authorization')
    google_validate_id_token(id_token=id_token)

    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user, _ = user_get_or_create(**serializer.validated_data)

    return Response(serializer.data)
