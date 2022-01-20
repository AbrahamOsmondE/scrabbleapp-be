from users.models import User
from .models import Puzzle
from rest_framework import serializers


class PuzzleSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='google_id', write_only=True)

    class Meta:
        model = Puzzle
        fields = ['user', 'letters', 'errors',
                  'correct_answers', 'possible_answers']

    def create(self, validated_data):
        user = validated_data.pop('user')
        puzzle = Puzzle.objects.create(user=user, **validated_data)
        return puzzle
