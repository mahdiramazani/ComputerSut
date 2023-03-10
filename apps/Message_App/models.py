from django.db import models
from apps.Acount_app.models import Teacher,User
from scripts.utils import jalali_convert
from apps.Course_app.models import Courses

class MessageModel(models.Model):

    user=models.ManyToManyField(User,related_name="message")
    sender=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="message")
    courses=models.ManyToManyField(Courses,related_name="message")
    created=models.DateTimeField(auto_now_add=True)
    titel=models.CharField(max_length=100)
    body=models.TextField()


    def get_jalali_date(self):


        return jalali_convert(self.created)

    def __str__(self):


        return self.body
