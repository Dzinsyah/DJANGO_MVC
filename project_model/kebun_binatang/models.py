from django.db import models
from django.utils import timezone


class Hewan(models.Model):
    nama = models.CharField(max_length =100)
    spesies = models.CharField(max_length =100)
    berat = models.CharField(max_length =10)
    umur = models.CharField(max_length =10)
    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length =100)
    isi_kandang = models.CharField(max_length =125)
    luas_kandang = models.CharField(max_length =50)
    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length =100)
    nomor_telepon = models.CharField(max_length =15)
    jadwal_jaga = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length =100)
    nomor_telepon = models.CharField(max_length =15)
    hari_berkunjung = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama
# Create your models here.
