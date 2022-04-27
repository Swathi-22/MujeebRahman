from multiprocessing import context
import re
from django.shortcuts import  render,get_object_or_404
from .forms import ContactForm
from .models import Contact,Gallery,Update,Companies
from django.http import JsonResponse

# Create your views here.

def index(request):
    updates=Update.objects.all()[:3]
    company=Companies.objects.all()
    context = {
        "is_index" : True,
        'updates':updates,
        'company':company
    }
    return render(request,'web/index.html',context)


def profile(request):
    context = {
        "is_profile" : True,
    }
    return render(request,'web/profile.html',context)


def position(request):
    context = {
        "is_position" : True,
    }
    return render(request,'web/position.html',context)


def award(request):
    context = {
        "is_award" : True,
    }
    return render(request,'web/award.html',context)


def companies(request):
    context = {
        "is_companies" : True,
    }
    return render(request,'web/companies.html',context)


def services(request):
    context = {
        "is_service" : True,
    }
    return render(request,'web/services.html',context)


def updates(request):
    updates=Update.objects.all()
    context = {
        "is_updates" : True,
        'updates':updates
    }
    return render(request,'web/updates.html',context)


def updateDetails(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.all()
    context = {
        'update':update,
        'updates':updates
    }
    return render(request,'web/update-details.html',context)


def gallery(request):
    gallery=Gallery.objects.all()
    context = {
        "is_gallery" : True,
        'gallery':gallery
    }
    return render(request,'web/gallery.html',context)


def contact(request):
    forms=ContactForm(request.POST or None)
    context = {
        "is_contact" : True,
        'forms':forms
    }
    return render(request,'web/contact.html',context)


def SaveContactForm(request):
    forms=ContactForm(request.POST or None)
    if request.method=='POST':
        print(request.POST)
        if forms.is_valid():
            forms.save()
    return JsonResponse({'title':'name'})