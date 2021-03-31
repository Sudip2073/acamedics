from django.urls import path
from . import views

urlpatterns = [
    path('',views.dash, name = "dash"),
    path('guidelines/',views.guide),
    path('about/',views.about)

]
