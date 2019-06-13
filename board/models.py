from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',default='photos/no_img.png')