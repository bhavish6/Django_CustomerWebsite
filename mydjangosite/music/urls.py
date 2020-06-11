from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/',views.userPage,name="userpage"),
    path('', views.home,name='home'),
    path('products/', views.products,name='products'),
    path('customer/<int:pk>/', views.getcustomer,name='customer'), #the angular brackets are djangos way of dynamic url, & the parameter passed is same as in views.py
    path('createorder/<str:pk>/',views.createorder,name='createorder'),
    path('updateorder/<str:pkey>/',views.updateorder, name='updateorder'),
    path('deleteorder/<str:pk>/',views.deleteorder, name='deleteorder'),
]