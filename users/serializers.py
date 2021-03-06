from puzzles.serializers import PuzzleSerializer
from .models import User
from rest_framework import serializers
from rest_framework.response import Response


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    google_id = serializers.CharField(required=False, default='')
    first_name = serializers.CharField(required=False, default='')
    last_name = serializers.CharField(required=False, default='')


class UserPuzzleSerializer(serializers.ModelSerializer):
    puzzles = PuzzleSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'puzzles']
