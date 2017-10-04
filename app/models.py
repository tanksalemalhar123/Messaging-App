from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AppUser(models.Model):
    user=models.OneToOneField(User,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default="profile_pics/default.png")
    contact=models.CharField(max_length=10,default='')
    contact_list=models.ManyToManyField('self', null=True)

    def __str__(self):
        return str(self.id)

class Message(models.Model):
    sender=models.ForeignKey(AppUser,null=True,related_name='sender')
    receiver=models.ForeignKey(AppUser,null=True,related_name='receiver')
    text=models.TextField(default='')
    timestamp=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.timestamp) + ' ' + self.text
