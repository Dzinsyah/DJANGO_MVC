from django.shortcuts import render
from .models import Mentee

def mentee(request):
    add_post = Mentee.objects.all()
    return render(request, 'mentee/mentee.html',{'mentee':add_post})


