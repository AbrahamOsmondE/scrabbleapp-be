from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
    path('userpuzzle', views.getUserPuzzle, name='userpuzzle')
]
