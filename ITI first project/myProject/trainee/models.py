from django.db import models
from track.models import Track

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    photo = models.ImageField(upload_to='trainee/images')
    statue = models.BooleanField(default=False)
    