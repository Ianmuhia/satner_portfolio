from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cv', views.cv, name='cv'),
    path('generate_pdf', views.generate_pdf, name='generate_pdf'),

    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('portfolio_home', views.portfolio_home, name='portfolio_home'),
    path('portfolio_details', views.portfolio_details, name='portfolio_details')

]
