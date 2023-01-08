from django.db import models
from apps.Acount_app.models import User



POSITION=(

    ("مدیر سایت و توسعه دهنده بک اند","مدیر سایت و توسعه دهنده بک اند"),
    ("توسعه دهنده فرانت اند","توسعه دهنده فرانت اند"),
    ("مدیر سئو","مدیر سئو"),
    ("مشاور و ایده پرداز","مشاور و ایده پرداز"),
    ("متخصص امنیت و شبکه","متخصص امنیت و شبکه"),
    ("برنامه نویس","برنامه نویس"),
    ("برنامه نویس ارشد","برنامه نویس ارشد"),
)


class TechnicalModel(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="technicalteam")
    created=models.DateTimeField(auto_now_add=True)
    postion=models.CharField(max_length=250,choices=POSITION,default="تیم فنی")


    def __str__(self):


        return self.user.phone


