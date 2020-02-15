from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from rest_framework import serializers
# Create your models here.

class UserDetail(models.Model):
    idno=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length=50)
    phno=PhoneNumberField()
    type = models.CharField(max_length=10,choices=[('S','Student'),('F','Faculty')])
    email=models.EmailField()
    year=models.CharField(max_length=1)
    def __str__(self):
        return self.idno

class Channel(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=30,unique=True)
    creationDate=models.DateField(default=timezone.now)
    description=models.TextField(max_length=100)
    channel_type = models.CharField(max_length=10,choices=[('R','Private'),('U','Public')],default='U')
    def __str__(self):
        return self.channel_name +" Channel"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=[('S','Student'),('F','Faculty')])
    channels=models.ManyToManyField(Channel)
    profilePicture = models.ImageField(default='default.png', upload_to='profile_pics')
    activated=models.BooleanField(default=False)
    email=models.EmailField()
    def __str__(self):
        return self.user.username + " Profile"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Post(models.Model):
    posted_in= models.ForeignKey(Channel, on_delete=models.CASCADE)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(null=True, blank=True, max_length=100)
    caption = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='post_images/',null=True,blank=True)
    files = models.FileField(upload_to='posts/', null=True, blank=True)

class Comments(models.Model):
    commented_post=models.ForeignKey(Post,on_delete=models.CASCADE)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()





