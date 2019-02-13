from django.db import models
from django.utils import timezone

class Mentee(models.Model):
    nama_mentee = models.CharField(max_length =100)
    images = models.CharField(max_length =255)
    description = models.TextField(max_length =1000)
    def __str__(self):
        return self.nama_mentee

# Create your models here.
