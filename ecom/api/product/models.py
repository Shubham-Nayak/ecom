from django.db import models
from api.category.models import Category
# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True) 
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=2500,blank=True,null=True)
    price=models.CharField(max_length=50)
    stock=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True,blank=True)
    images=models.ImageField(upload_to='images/',blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    def __str__(self):
        return self.name
