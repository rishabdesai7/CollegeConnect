from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Channel(models.Model):
    #createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,unique=True)
    creationDate=models.DateField(default=datetime.date.today())
    description=models.TextField(max_length=100)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=[('S','Student'),('F','Faculty')],default='S')
    uid = models.CharField(max_length=10,default='')
    joindate = models.DateField(null=True)
    channels=models.ManyToManyField(Channel,null = True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)












