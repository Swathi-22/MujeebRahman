from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "is_index" : True,
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
    context = {
        "is_updates" : True,
    }
    return render(request,'web/updates.html',context)


def updateDetails(request):
    context = {
        
    }
    return render(request,'web/update-details.html',context)


def gallery(request):
    context = {
        "is_gallery" : True,
    }
    return render(request,'web/gallery.html',context)


def contact(request):
    context = {
        "is_contact" : True,
    }
    return render(request,'web/contact.html',context)