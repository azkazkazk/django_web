from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from cw1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('', views.index),
    path('login/', views.login),
    path('rate/', views.rate),
    path('list/', views.list_),
    path('view/', views.view),
    path('average/', views.average),
    path('repassword/', views.re_password),
]
