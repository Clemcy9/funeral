from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.

relation = [
    ('', 'Select relationship status'),
    ('son', 'son'),
    ('daughter', 'daughter'),
    ('son_inlaw', 'son inlaw'),
    ('daughter_inlaw', 'daughter inlaw'),
    ('grand_child','grand child'),
    ('sibling', 'sibling'),
    ('friends', 'friends'),
    ('family_friend', 'family friend'),
    ('friends_of_children', 'friends of children')
]

class ImagePost(models.Model):
    # title = models.CharField(max_length=30)
    # image = models.ImageField(upload_to='./static/uploads')
    # image = CloudinaryField('image')
    caption = models.CharField(max_length=30, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    # def __str__(self) -> str:
    #     return self.date
    
class Tribute(models.Model):
    writer = models.CharField(verbose_name='your name', max_length=30)
    relationship = models.CharField( max_length=30,null=True, blank=True, choices=relation)
    tribute = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.writer 

class TributeComment(models.Model):
    commenter = models.CharField(verbose_name= 'Your name', max_length=30)
    comment = models.TextField()
    tribute = models.ForeignKey(to=Tribute, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.commenter + str(self.date)

class ImageComment(models.Model):
    commenter = models.CharField(verbose_name='Your name', max_length=30)
    comment = models.TextField()
    image = models.ForeignKey(to=ImagePost, on_delete= models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.commenter