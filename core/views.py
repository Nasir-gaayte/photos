from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')



def add(request):
    return render(request,'core/add.html')

def photo(request,pk):
    return render(request,'core/photo.html')