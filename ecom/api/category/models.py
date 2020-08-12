from django.db import models

# Create your models here.
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True) 
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=250,blank=True,null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    def __str__(self):
        return self.name
