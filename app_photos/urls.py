from django.urls import path
from . import views

urlpatterns = [
    path('', views.photos_album, name='photos_album'),
    path('2', views.page_2, name='page_2'),
    path('3', views.page_3, name='page_3'),
    path('4', views.page_4, name='page_4'),
    path('5', views.page_5, name='page_5'),
    path('6', views.page_6, name='page_6'),
    path('7', views.page_7, name='page_7'),
    path('8', views.page_8, name='page_8'),
]

