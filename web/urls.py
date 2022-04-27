from unicodedata import name
from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('profile/', views.profile,name='profile'),
    path('position/', views.position,name='position'),
    path('award/', views.award,name='award'),
    path('companies/', views.companies,name='companies'),
    path('services/', views.services,name='services'),
    path('updates/', views.updates,name='updates'),
    path('update-details/<str:slug>/', views.updateDetails,name='updateDetails'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
    path('SaveContactForm/', views.SaveContactForm,name='SaveContactForm'), 
]