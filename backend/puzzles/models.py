from django.db import models
from users.models import User
# Create your models here.


class Puzzle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    letters = models.CharField(max_length=7, blank=False)
    errors = models.IntegerField()
    correct_answers = models.IntegerField()
    possible_answers = models.IntegerField()

    def __str__(self):
        return self.letters
