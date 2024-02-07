from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.projects, name='projects'),
    path('contact', views.contactForm, name='contact'),
    path('about', views.about, name='about'),
]