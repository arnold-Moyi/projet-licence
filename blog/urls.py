import django
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from prfe import settings
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home),
    path('home/', views.home, name='home'),
    path('Login/', views.Login, name='login'),
    path('About/', views.About, name='about'),
    path('Formulaire/', views.Formulaire, name='form'),
    path('Connect/', views.Connect, name='connexion'),
    path('Dashboard/', views.Dashboard, name='accueil'),
    path('SeDeconnecter/', views.SeDeconnecter, name='déconnexion'),
    path('password/', views.Change_password, name='password'),
    path('EditProfile/', views.EditProfile, name='edit_profile'),
    path('info/', views.info, name='informatique'),
    path('Math/', views.Math, name='mathematique'),
    path('Bio/', views.Bio, name='biologie'),
    path('Licence/', views.Licence, name='licence'),
    path('Master/', views.Master, name='master'),
    path('Doctorat/', views.Doctorat, name='doctorat'),
    path('Football/', views.Foot, name='football'),
    path('Basket/', views.Basket, name='basketball'),
    path('Judo/', views.Judo, name='judo'),
    path('liste_livre/', views.liste_livre, name='liste'),
    path('Search/', views.recherche, name='search'),
    path('Review/', views.reviews_livre, name='review'),
    path('Review_memoire/', views.reviews_memoire, name='review_memoire'),
    path('Review_article/', views.reviews_article, name='review_article'),
    path('Avis_livre/', views.Avis_livre, name='avis_livre'),
    path('Avis_memoire/', views.Avis_memoire, name='avis_memoire'),
    path('Avis_article/', views.Avis_article, name='avis_article'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
