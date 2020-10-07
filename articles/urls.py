
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.article_list, name='articles'),
    path('articles/<str:slug>', views.article_details, name='article'),

]

urlpatterns += staticfiles_urlpatterns()
