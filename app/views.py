from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('halaman satu.')

def berita1(request):
    return render(request, 'berita1.html')

def berita2(request):
    return render(request, 'berita2.html')
