from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('berita1', views.berita1, name='berita1'),
    path('berita2', views.berita2, name='berita2'),
]

