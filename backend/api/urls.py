from django.urls import path
from . import views

urlpatterns = [
    path('words/<str:word>', views.getWords, name='words')

]
