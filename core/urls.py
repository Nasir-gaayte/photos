from django.urls import path 
from . import views 



urlpatterns = [
    path('',views.home,name='home'),
    path('photo/<str:pk>/',views.photo,name='photo'),
    path('add/',views.add,name='add'),
    # path('add/',views.AddPhoto.as_view(),name='add'),
    path('update/<id>/',views.update,name='update'),
]
