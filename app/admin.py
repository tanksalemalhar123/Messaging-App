from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(AppUser)
admin.site.register(Message)
admin.site.register(TextMsg)
admin.site.register(FileMsg)
admin.site.register(ImageMsg)
