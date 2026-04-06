from django.urls import path
from . import views

urlpatterns = [
    path('', views.videogame_list, name='videogame_list'),
    path('<int:pk>/', views.videogame_detail, name='videogame_detail'),
    path('create/', views.videogame_create, name='videogame_create'),
    path('<int:pk>/update/', views.videogame_update, name='videogame_update'),
    path('<int:pk>/delete/', views.videogame_delete, name='videogame_delete'),
]
