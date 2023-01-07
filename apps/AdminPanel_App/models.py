from django.db import models
from apps.Acount_app.models import User

POSITION=(
    ("عضویت در کادر فنی","عضویت در کادر فنی"),
    ("وبلاگ نویس","وبلاگ نویس"),
    ("مدرس","مدرس"),
    ("کارمند","کارمند"),
)

class RequestsModel(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Requests")
    introduction=models.TextField()
    position=models.CharField(max_length=100,choices=POSITION)
    resume=models.FileField(upload_to="media/request")
    is_technical_team = models.BooleanField(default=False)
    is_blogger = models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_employee=models.BooleanField(default=False)

    def __str__(self):


        return self.user.full_name