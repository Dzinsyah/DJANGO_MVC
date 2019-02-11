from django.db import models
from django.utils import timezone

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length =100)
    nomor_telepon = models.CharField(max_length =14)
    jabatan = models.CharField(max_length =100)
    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length =100)
    nomor_telepon = models.CharField(max_length =14)
    nomor_absen = models.CharField(max_length =5)
    nilai_rata_rata = models.CharField(max_length =50)
    def __str__(self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length =100)
    jadwal_dimulai = models.DateTimeField(default=timezone.now) 
    jadwal_berakhir = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama_pelajaran
        
class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length =100)
    nomor_telepon = models.CharField(max_length =14)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length =100)
    banyak_soal = models.CharField(max_length =50)
    bobot_nilai = models.CharField(max_length =100)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_challenge

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length =100)
    banyak_soal = models.CharField(max_length =50)
    bobot_nilai = models.CharField(max_length =100)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama_live_code