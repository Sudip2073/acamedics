from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginpage, name = 'login'),
    path('logout',views.logoutuser, name = 'logout'),
    path('registration/',views.register)
]
