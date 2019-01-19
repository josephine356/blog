from django.urls import path
from watch import views


app_name = 'watch'
urlpatterns = [
    path('', views.watch, name='watch'),
    path('watchCreate/', views.watchCreate, name='watchCreate'),
    path('watchRead/<int:watchId>/', views.watchRead, name='watchRead'),
    path('watchUpdate/<int:watchId>/', views.watchUpdate, name='watchUpdate'),
    path('watchDelete/<int:watchId>/', views.watchDelete, name='watchDelete'),
    path('watchSearch/', views.watchSearch, name='watchSearch'),
]