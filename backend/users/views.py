from django.shortcuts import render
import requests

from django.conf import settings
from .authentication import google_validate_id_token, jwt_login

from .selector import user_get_me
from .serializers import UserSerializer
from .services import user_get_or_create

from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from rest_framework.response import Response


GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'


@api_view(['POST'])
def login(request, *args, **kwargs):
    id_token = request.headers.get('Authorization')
    google_validate_id_token(id_token=id_token)

    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user, _ = user_get_or_create(**serializer.validated_data)

    response = Response(data=user_get_me(user=user))
    response = jwt_login(response=response, user=user)

    return response
