from django.db import models
from apps.Acount_app.models import User, Teacher
from django.urls import reverse
from scripts.utils import jalali_convert
from django.utils import timezone

LEVEL = (
    ("مقدماتی", "مقدماتی"),
    ("مقدماتی تا پیشرفته", "مقدماتی تا پیشرفته"),
    ("پیشرفته", "پیشرفته"),
    ("پروژه محور و مقدماتی", "پروژه محور و مقدماتی"),
    ("پیشرفته و پروژه محور", "پیشرفته و پروژه محور"),
)

STATUS = (

    ("درحال برگزاری...", "درحال برگزاری..."),
    ("تکمیل شده", "تکمیل شده"),

)


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="image/category_image", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_jalali_date(self):

        return jalali_convert(self.created)


class Courses(models.Model):

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="Corses")
    cover = models.FileField(upload_to="media/video_cover")
    introduction_video = models.FileField(upload_to="media/Video")
    user = models.ManyToManyField(User, related_name="Corses", null=True, blank=True)
    titel = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=LEVEL, default="مقدماتی")
    price = models.IntegerField(default=0)
    discount = models.IntegerField(null=True, blank=True,default=None)
    view = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, related_name="Corses")
    specifications = models.TextField()
    Introduction_of_the_valley = models.TextField()
    project_count = models.CharField(max_length=50, default="0")
    slug = models.SlugField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS,default="در حال برگزاری...")
    discount=models.IntegerField(null=True,blank=True)


    def get_absulot_url(self):
        return reverse("Course_app:Course_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.titel




class CoursesChild(models.Model):
    parent = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="corses_child")
    introduction = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to="media/video", null=True, blank=True)
    video_cover = models.ImageField(upload_to="media/video_cover", null=True, blank=True)
    link_video = models.CharField(max_length=500, null=True, blank=True, default="aparat.com")
    time = models.CharField(max_length=50, default="00:00")
    topic = models.CharField(max_length=100)
    topic_parent = models.ForeignKey("self", related_name="Course_app_CoursesChild_topic_parent",
                                     on_delete=models.CASCADE, null=True, blank=True)
    status=models.BooleanField(default=True)


    def get_absolut_url(self):
        return reverse("Course_app:video_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.topic




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment")
    corses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="Comment")
    body = models.TextField()



    def __str__(self):

        return self.body[:10]



