#from django.db.models import CharField
#from django.db.models import TextField
from django.db import models
from django.utils import timezone

class Mentee(models.Model):
    name = models.CharField(max_length =255)
    full_name = models.TextField(max_length =255)
    gender = models.CharField(max_length =1)
    telephone = models.TextField(max_length =25)
    mobile = models.TextField(max_length =25)
    address = models.TextField(max_length =255)
    nickname = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
# Create your models here.

class BlogPost(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length =255)
    content = models.CharField(max_length =255)
    created_by = models.CharField(max_length =50)
    posted_by = models.ForeignKey(Mentee,on_delete=models.CASCADE)


