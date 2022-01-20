from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from users.models import User

from .serializers import PuzzleSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def submitPuzzle(request):
    serializer = PuzzleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
