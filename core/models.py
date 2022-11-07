from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    
class PhotoModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete = models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField(max_length=500, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.description
        