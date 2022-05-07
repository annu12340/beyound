from django.urls import path
from . import views


urlpatterns = [
    path('', views.qrcode, name='qrcode'),

]
