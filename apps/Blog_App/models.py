from django.db import models
from apps.Acount_app.models import User
from apps.Course_app.models import Category
from scripts.utils import jalali_convert
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField

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
    status=models.BooleanField(default=True)


    class Meta:

        ordering=("-created",)

    def get_absolut_url(self):


        return reverse("Blog_App:blog_detail",kwargs={"pk":self.id})





    def get_jalali_date(self):


        return jalali_convert(self.created)

    def __str__(self):

        return self.titel


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Comment_blog")
    blog=models.ForeignKey(BlogModel,on_delete=models.CASCADE,related_name="comment")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replay",null=True,blank=True)


    class Meta:
        ordering=("-created",)

    def __str__(self):


        return self.user.full_name


