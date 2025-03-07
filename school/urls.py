
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('contact/', views.contactpage, name='contact'),
    path('about/', views.aboutpage, name='about'),
    path('detail/', views.detailspage, name='detail'),
    path('dashboard/', views.dashboardpage,name='dashboard'),
    path('register/', views.registerpage,name='register'),
    path('success/', views.successpage,name='success'),

]
