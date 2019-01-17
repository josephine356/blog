from django.urls import path
from good import views


app_name = 'good'
urlpatterns = [
    path('mac', views.mac, name='mac'),
    path('ipad', views.ipad, name='ipad'),
    path('iphone', views.iphone, name='iphone'),
    path('watch', views.watch, name='watch'),
]