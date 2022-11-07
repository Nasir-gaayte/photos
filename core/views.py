from django.shortcuts import render
from .models import CategoryModel, PhotoModel
# Create your views here.

def home(request):
    galarys = PhotoModel.objects.all()
    return render(request,'core/home.html',{'galarys':galarys})



def add(request):
    return render(request,'core/add.html')

def photo(request,pk):
    return render(request,'core/photo.html')