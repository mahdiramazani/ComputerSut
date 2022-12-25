from django.db import models
from apps.Acount_app.models import User
from apps.Course_app.models import Category
from scripts.utils import jalali_convert


class Tag(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def get_jalali_date(self):

        return jalali_convert(self.created)

    def __str__(self):

        return self.name


class BlogModel(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="blog",null=True,blank=True)
    titel=models.CharField(max_length=200)
    view=models.IntegerField(default=0)
    image=models.FileField(upload_to="media/blog/image")
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    category=models.ManyToManyField(Category,related_name="blog")


    def get_jalali_date(self):


        return jalali_convert(self.created)

    def __str__(self):

        return self.titel
