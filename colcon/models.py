from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
'''
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
'''
class UserDetails(models.Model):
    rollno=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    father_phno=PhoneNumberField(null=True,blank=True)#models.CharField(max_length=10)
    mather_phno=PhoneNumberField(null=True,blank=True)#models.CharField(max_length=10)
    phno=PhoneNumberField()
    permanent_add=models.TextField()
    permanent_add_pincode=models.CharField(max_length=6)
    current_add = models.TextField(null=True,blank=True)
    current_add_pincode = models.CharField(max_length=6.null=True,blank=True)
    adhaar_card=models.CharField(max_length=12)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    year=models.CharField(max_length=1)
    def __str__(self):
        return self.rollno

class Channel(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=30,unique=True)
    creationDate=models.DateField(default=datetime.date.today())
    description=models.TextField(max_length=100)
    def __str__(self):
        return self.channel_name +" Channel"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=[('S','Student'),('F','Faculty')])
    channels=models.ManyToManyField(Channel)
    profilePicture = models.ImageField(default='default.png', upload_to='profile_pics')
    def __str__(self):
        return self.user.name + " Profile"

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
    files = models.FileField(upload_to='posts/', null=True, blank=True)

class Comments(models.Model):
    commented_post=models.ForeignKey(Post,on_delete=models.CASCADE)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()












