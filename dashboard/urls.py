from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dash, name = "dash"),
    path('guidelines/',views.guide),
    path('about/',views.about),
    path('',views.home),

]
