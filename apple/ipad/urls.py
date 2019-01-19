from django.urls import path
from ipad import views


app_name = 'ipad'
urlpatterns = [
    path('', views.ipad, name='ipad'),
    path('ipadCreate/', views.ipadCreate, name='ipadCreate'),
    path('ipadRead/<int:ipadId>/', views.ipadRead, name='ipadRead'),
    path('ipadUpdate/<int:ipadId>/', views.ipadUpdate, name='ipadUpdate'),
    path('ipadDelete/<int:ipadId>/', views.ipadDelete, name='ipadDelete'),
    path('ipadSearch/', views.ipadSearch, name='ipadSearch'),
]