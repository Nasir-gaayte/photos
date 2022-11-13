from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    
class PhotoModel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete = models.CASCADE)
    image = models.ImageField(null=False, blank=False, upload_to="images/")
    description = models.TextField(max_length=500, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.description
        