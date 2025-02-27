from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
