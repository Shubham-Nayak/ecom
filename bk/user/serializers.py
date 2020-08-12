from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes,permission_classes
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        # return Comment.objects.create(**validated_data)
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


    def update(self, instance, validated_data):
        # instance.email = validated_data.get('email', instance.email)
        # instance.content = validated_data.get('content', instance.content)
        # instance.created = validated_data.get('created', instance.created)
        for attr,value in validated_data.items():
            if attr =='password':
                instance.set_password(value)
            else:
                setattr(instance,attr,value)
        instance.save()
        return instance

    class Meta:
        model=CustomUser
        extra_kwargs={'password':{'write_only':True}}
        fields=('name','email','password','phone','gender','is_active','is_staff','is_superuser')