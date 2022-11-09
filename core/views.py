from django.shortcuts import render, redirect
from .models import CategoryModel, PhotoModel
from .forms import PhotoAddForm
from django.views import generic
from django.views.generic import CreateView
# Create your views here.

def home(request):
    photos = PhotoModel.objects.all()
    cats = CategoryModel.objects.all()
    return render(request,'core/home.html',{
        'photos':photos,
        'cats':cats,
        })



def add(request):
    cats = CategoryModel.objects.all()
    if request.method=="POST":
        data = request.POST
        image = request.FILES.get('image') 
        if data["category"] != 'none':
            category = CategoryModel.objects.get(id= data['category'])
        elif data['category_new'] != '':
            category, create= CategoryModel.objects.get_or_create(name= data['category_new'])
        else:
            category = None
        photo = PhotoModel.objects.get_or_create (
            category = category,
            description= data['description'],
            image = image,
        )  
        return redirect ('home')        
    return render(request,'core/add.html',{
        
        'cats':cats,
        })

# class AddPhoto(generic.CreateView):
#     model= PhotoModel
#     form_class = PhotoAddForm
#     template_name = 'core/add.html'
#     success_url= 'core/home.html'





def photo(request,pk):
    photos= PhotoModel.objects.get(id=pk)
    return render(request,'core/photo.html',{
        'photos':photos,
    })