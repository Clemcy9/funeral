from django.contrib import admin
from .models import ImagePost, Tribute, TributeComment, ImageComment

# Register your models here.

admin.site.register([ImagePost, TributeComment,Tribute, ImageComment])