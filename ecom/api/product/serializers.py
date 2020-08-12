from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    images=serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
    class Meta:
        model=Product
        fields=('product_id','name','description','price','stock','images','category')