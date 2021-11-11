from django.urls import path
from . import views

urlpatterns = [
    path('wordbuilder/<str:word>', views.getWords, name='wordbuilder'),
    path('anagram/<str:word>', views.getAnagram, name='anagram'),
    path('startingwith/<str:word>', views.getStartingWith, name='startingwith'),
    path('endingwith/<str:word>', views.getEndingWith, name='endingwith'),
    path('containing/<str:word>', views.getContaining, name='containingwith'),

]
