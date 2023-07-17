
from django.contrib import admin
from django.urls import path, include
from appbank import views
app_name='appbank'
urlpatterns = [
    path('',views.home,name='home'),

]