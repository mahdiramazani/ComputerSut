from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from apps.Teacher_app.models import Teacher

@receiver(post_delete,sender=Teacher)
def delete_teacher(sender,instance,**kwargs):

    user=instance.user
    user.is_teacher = False

    user.save()

