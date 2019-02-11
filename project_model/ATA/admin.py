from django.contrib import admin
from .models import Direksi, Mentee, MataPelajaran, Mentor, Challenge, LiveCode

my_model = [Direksi, Mentee, MataPelajaran, Mentor, Challenge, LiveCode]
admin.site.register(my_model)
# Register your models here.
