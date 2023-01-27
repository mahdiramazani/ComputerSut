from django.db import models
from apps.Acount_app.models import Teacher
from apps.Course_app.models import Courses


class TeachersIncome(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="teacher_income")
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,related_name="teacher_income")
    income=models.IntegerField(default=0)
    status=models.BooleanField(default=False)


    def __str__(self):

        return self.teacher.user.full_name
