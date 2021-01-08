from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1) 
    thumbnail=models.FileField(upload_to="posts/",null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title
    class Meta:
        db_table='posts'
        verbose_name='Post'
        verbose_name_plural='Posts'
        ordering=['-created_at']


class Category(models.Model):
    title = models.CharField(  max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title
    class Meta:
        db_table='categories'
        verbose_name='Category' 
        verbose_name_plural='Categories'
        ordering=['-created_at']


class PostsForm(forms.ModelForm):
    class Meta:
        model= Posts
        fields= ['title','content','thumbnail','user']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Post Title'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Content'}),
            'thumbnail':forms.FileInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
        }
        help_texts={
            'title':'Enter Title Here',
        }
        error_messages={}
        labels={
            'title':'Enter Post Title',
        }
    def clean(self):
        fields= self.cleaned_data
        keys=list(fields.keys())
        if(len(fields['title'])<=10):
            raise ValidationError("%(val) Must Be Greater Than 10",params={'val':keys[0]})
        if(len(fields['content'])<=10):
            raise ValidationError("%(val) Must Be Greater Than 10",params={'val':keys[1]})
