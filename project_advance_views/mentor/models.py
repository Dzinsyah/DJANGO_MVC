from django.db import models
from django.utils import timezone

class Mentor(models.Model):
    nama_mentor = models.CharField(max_length =100)
    images = models.CharField(max_length =255)
    position = models.CharField(max_length =255)
    description = models.TextField(max_length =1000)
    def __str__(self):
        return self.nama_mentor

# Create your models here.
