from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('add', views.add, name='add'),
    path('sign', views.sign, name='sign'),
]