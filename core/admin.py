from django.contrib import admin
from .models import CategoryModel, PhotoModel

# Register your models here.


admin.site.register(CategoryModel)
admin.site.register(PhotoModel)