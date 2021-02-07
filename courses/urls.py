from django.urls import path
from . import views

urlpatterns = [
    path('',views.courses),
    path('year<int:mod_year>/',views.modules),
    path('<str:Mod_code>',views.modules_detail, name='modules_detail'),
]
