from django.db import models
from django.utils import timezone

class Blog(models.Model):
    nama = models.CharField(max_length =100)
    images = models.CharField(max_length =255)
    title = models.CharField(max_length =255)
    content = models.TextField(max_length =1000)
    def __str__(self):
        return self.nama

# Create your models here.
