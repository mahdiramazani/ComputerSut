import os
from django.conf import settings
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
    ("به زودی", "به زودی"),

)
How_TO_HOLD=(
    ("آنلاین","آنلاین"),
    ("حضوری","حضوری"),
)

def STR_TO_LIST(string):

    new_list=[]

    for item in string:

        new_list.append(item)

    return new_list

def LIST_TO_STR(LIST):

    new_str=""

    for item in LIST:

        new_str += item

    return new_str

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="image/category_image", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absulot_url(self):


        return reverse("Course_app:Category_course",kwargs={"id":self.id})

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
    how_to_hold=models.CharField(max_length=100,choices=How_TO_HOLD,default="آنلاین")
    created = models.DateTimeField(auto_now_add=True)
    capacity=models.IntegerField(default=0)

    def get_price(self):

        if self.price >= 1100 and self.price <= 9999:

            new_price = ""

            new_price += str(self.price)

            new_price = STR_TO_LIST(new_price)

            new_price[-4] += ","

            new_price = LIST_TO_STR(new_price)

            return new_price

        elif self.price >= 10000 and self.price <= 99999:

            new_price = ""

            new_price += str(self.price)

            new_price = STR_TO_LIST(new_price)

            new_price[1] += ","

            new_price = LIST_TO_STR(new_price)

            return new_price

        elif self.price >= 100000 and self.price <= 999999:

            new_price = ""

            new_price += str(self.price)

            new_price = STR_TO_LIST(new_price)

            new_price[-4] += ","


            new_price = LIST_TO_STR(new_price)

            return new_price


        elif self.price >= 1000000:

            new_price = ""

            new_price += str(self.price)

            new_price = STR_TO_LIST(new_price)

            new_price[-4] += ","
            new_price[-7] += ","

            new_price = LIST_TO_STR(new_price)

            return new_price
        else:
            return self.price


    def get_jalali_date(self):

        return jalali_convert(self.created)


    def get_absulot_url(self):
        return reverse("Course_app:Course_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.titel


#unview

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
    lock=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def get_jalali_date(self):
        return jalali_convert(self.created)


    def get_absolut_url(self):
        return reverse("Course_app:video_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.topic




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment")
    corses = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="Comment")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def get_jalali_date(self):
        return jalali_convert(self.created)



    def __str__(self):

        return self.body[:10]


class CertificatesOfCourses(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="CertificatesOfCourses")
    document_number=models.CharField(max_length=100,unique=True)
    course=models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True,blank=True,related_name="CertificatesOfCourses")
    image_document=models.FileField(upload_to="media/course/document/image")
    document=models.FileField(upload_to="media/course/document")
    created=models.DateTimeField(auto_now_add=True)




    def __str__(self):


        return self.user.full_name

    def get_jalali_date(self):

        return jalali_convert(self.created)



class Checkout(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="checkout")
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,related_name="checkout")
    price=models.IntegerField()
    is_paid=models.BooleanField(default=False)


    def get_price(self):


        if self.price >= 11000 and self.price <= 99999 :

            new_price=""

            new_price += str(self.price)


            new_price=STR_TO_LIST(new_price)

            new_price[-4] += ","

            new_price=LIST_TO_STR(new_price)

            return new_price

        elif self.price >= 100000 and self.price <= 999999 :

            new_price=""

            new_price += str(self.price)


            new_price=STR_TO_LIST(new_price)

            new_price[2] += ","

            new_price=LIST_TO_STR(new_price)

            return new_price

        elif self.price >= 1000000 and self.price <= 9999999:

            new_price = ""

            new_price += str(self.price)


            new_price = STR_TO_LIST(new_price)

            new_price[-4] += ","
            new_price[-7] += ","

            new_price = LIST_TO_STR(new_price)

            return new_price


        elif self.price >= 10000000:

            new_price = ""

            new_price += str(self.price)


            new_price = STR_TO_LIST(new_price)

            new_price[-4] += ","
            new_price[-7] += ","


            new_price = LIST_TO_STR(new_price)

            return new_price

        else:

            return self.price




    def __str__(self):

        return self.user.full_name
