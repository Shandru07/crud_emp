from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add_emp,name='add'),
    path('up/<int:pk>/',views.up_emp,name='up'),
    path('dlt/<int:pk>/',views.dlt_emp,name='dlt'),
]
