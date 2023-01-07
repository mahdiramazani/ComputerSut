from django.db import models


class ContactUs(models.Model):
    full_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    created=models.DateTimeField(auto_now_add=True)
    body=models.TextField()


    def __str__(self):


        return f"{self.full_name} | {self.body[:20]}"
