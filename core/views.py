from django.shortcuts import render, redirect
from .models import CategoryModel, PhotoModel
from django.contrib.auth.models import User
from .forms import PhotoAddForm
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    phos=PhotoModel.objects.all()
    category = request.GET.get('category')
    if category == None:
        photos = PhotoModel.objects.all().order_by('-id')
    else:
        photos = PhotoModel.objects.filter(category__name=category)    
        print(category)
   
    categorys = CategoryModel.objects.all()
    return render(request,'core/home.html',{
        'photos':photos,
        'categorys':categorys,
        'phos':phos,
    })


def add(request):
    cats = CategoryModel.objects.all()
    if request.method=="POST":
        data = request.POST
        username = request.user
        images = request.FILES.getlist ('images') 
        if data["category"] != 'none':
            category = CategoryModel.objects.get(id= data['category'])
        elif data['category_new'] != '':
            category, create= CategoryModel.objects.get_or_create(name= data['category_new'])
        else:
            category = None
        for image in images:    
            photo = PhotoModel.objects.get_or_create (
                username = username,
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
    

@login_required    
def update(request, id):
    toup = PhotoModel.objects.get(pk=id)
    if request.method == "POST":
        form = PhotoAddForm(request.POST, instance=toup)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=PhotoAddForm(instance=toup)
    return render(request,'core/update.html',{'form':form})    
        
    
    
@login_required
def delete(request,id):
    to_delete = PhotoModel.objects.get(pk=id)
    if request.method == "POST":
        to_delete.delete()  
        return redirect('home')  
    return render(request,'core/delete.html',{'to_delete':to_delete})