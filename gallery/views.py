from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import Image

class GalleryView(ListView):
    model = Image
    template_name = 'gallery/gallery.html'







