from django.urls import path
from iphone import views


app_name = 'iphone'
urlpatterns = [
    path('', views.iphone, name='iphone'),
    path('iphoneCreate/', views.iphoneCreate, name='iphoneCreate'),
    path('iphoneRead/<int:iphoneId>/', views.iphoneRead, name='iphoneRead'),
    path('iphoneUpdate/<int:iphoneId>/', views.iphoneUpdate, name='iphoneUpdate'),
    path('iphoneDelete/<int:iphoneId>/', views.iphoneDelete, name='iphoneDelete'),
    path('iphoneSearch/', views.iphoneSearch, name='iphoneSearch'),
]