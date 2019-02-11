from django.db import models
from django.utils import timezone


class Dokter(models.Model):
    nama = models.CharField(max_length =100)
    nomor_telepon = models.CharField(max_length =25)
    bidang = models.CharField(max_length =100)
    jadwal_praktek = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length =100)
    nomor_telepon = models.CharField(max_length =25)
    alamat = models.CharField(max_length =150)
    keluhan = models.CharField(max_length =255)
    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length =100)
    total_harga = models.CharField(max_length =100)
    kumpulan_obat = models.CharField(max_length =100)
    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length =100)
    kandungan = models.CharField(max_length =255)
    khasiat = models.CharField(max_length =255)
    def __str__(self):
        return self.nama
# Create your models here.
