from django.urls import path
from . import views

urlpatterns = [
    path('', views.videogame_create, name='videogame'),
    path('<int:pk>/', views.videogame_detail, name='videogame_detail'),
    path('<int:pk>/update/', views.videogame_update, name='videogame_update'), 
    
]
