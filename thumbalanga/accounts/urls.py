from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name="home"),
    path('create_member/', views.create_member,name="create_member"),
    path('update_member/<str:pk_member>/', views.update_member,name="update_member"),
    path('delete_member/<str:pk_delete>/', views.delete_member,name="delete_member"),
     path('createLoan/', views.createLoan,name="createLoan"),
]

