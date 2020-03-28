from django.urls import path
from . import views

urlpatterns = [
    path('', views.photos_album, name='photos_album'),
]