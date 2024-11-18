from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    content = CKEditor5Field('Text', config_name='extends')
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    thumbnail = CloudinaryField('image')
    publish_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('publish_date',)
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
    