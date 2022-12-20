from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """


        user = self.model(
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone=phone,
            password=password,

        )

        user.is_admin = True
        user.save(using=self._db)
        return user


UNIVERSITY_NAME = (
    ("دانشگاه صنعتی سیرجان", "دانشگاه صنعتی سیرجان"),
    ("دانشگاه باهنر کرمان", "دانشگاه باهنر کرمان"),
    ("سایر دانشگاه ها", "سایر دانشگاه ها"),
)

MAJOR= (
    ("مهندسی کامپیوتر", "مهندسی کامپیوتر"),
    ("مهندسی برق", "مهندسی برق"),
    ("مهندسی شیمی", "مهندسی شیمی"),
    ("علوم کامپیوتر", "علوم کامپیوتر"),
    ("سایر رشته ها", "سایر رشته ها"),
)


class User(AbstractBaseUser):
    full_name=models.CharField(max_length=100)
    phone = models.CharField(
        verbose_name='شماره تلفن',
        max_length=13,
        unique=True
    )
    bio=models.TextField(null=True,blank=True)
    instagram=models.CharField(max_length=200,default="https://www.instagram.com/")
    twitter=models.CharField(max_length=200,default="https://www.twitter.com/")
    linkedin=models.CharField(max_length=200,default="https://www.linkedin.com/")
    facebook=models.CharField(max_length=200,default="https://www.facebook.com/")
    username=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to="media/user_image",null=True,blank=True)
    student_number = models.CharField(max_length=50,null=True,blank=True)
    university_name = models.CharField(choices=UNIVERSITY_NAME,max_length=100,default="دانشگاه صنعتی سیرجان")
    major=models.CharField(max_length=50,choices=MAJOR,default="مهندسی کامپیوتر")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Teacher(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Teacher")
    bio=models.TextField()
    position=models.CharField(max_length=100,null=True,blank=True)



    def __str__(self):


        return self.user.full_name