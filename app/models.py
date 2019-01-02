from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

class AppUser(models.Model):
    user=models.OneToOneField(User,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default="profile_pics/default.png")
    contact=models.CharField(max_length=10,default='')
    contact_list=models.ManyToManyField('self', null=True)

    def __str__(self):
        return str(self.id)

class Message(models.Model):
    TYPES = [
    ('TEXT', 'Text'),
    ('IMAGE', 'Image'),
    ('FILE', 'File')
    ]
    sender=models.ForeignKey(AppUser,null=True,related_name='sender')
    receiver=models.ForeignKey(AppUser,null=True,related_name='receiver')
    msg_type = models.CharField(choices=TYPES, max_length=10, null=True)
    timestamp=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.timestamp) + ' ' + self.msg_type

class TextMsg(models.Model):
    message = models.OneToOneField(Message, null=True)
    text=models.TextField(default='')

    def __str__(self):
        return str(self.id)

class ImageMsg(models.Model):
    message = models.OneToOneField(Message, null=True)
    image=models.ImageField(upload_to='chat_images/', null=True)

    def __str__(self):
        return str(self.id)

class FileMsg(models.Model):
    message = models.OneToOneField(Message, null=True)
    file_item = models.FileField(upload_to='chat_files/', null=True)

    def filename(self):
        return os.path.basename(self.file_item.name)

    def __str__(self):
        return str(self.id)
