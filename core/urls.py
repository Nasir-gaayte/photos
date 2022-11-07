from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.home,name='home'),
    path('photo/<str:pk>/',views.photo,name='photo'),
    path('add/',views.add,name='add'),
]