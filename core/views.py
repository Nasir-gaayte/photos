from django.shortcuts import render, redirect
from .models import CategoryModel, PhotoModel
from .forms import PhotoAddForm
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    category = request.GET.get('category')
    if category == None:
        photos = PhotoModel.objects.all()
    else:
        photos = PhotoModel.objects.filter(category__name=category)    
        print(category)
   
    categorys = CategoryModel.objects.all()
    return render(request,'core/home.html',{
        'photos':photos,
        'categorys':categorys,
    })


def add(request):
    cats = CategoryModel.objects.all()
    if request.method=="POST":
        data = request.POST
        images = request.FILES.getlist ('images') 
        if data["category"] != 'none':
            category = CategoryModel.objects.get(id= data['category'])
        elif data['category_new'] != '':
            category, create= CategoryModel.objects.get_or_create(name= data['category_new'])
        else:
            category = None
        for image in images:    
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
        
    