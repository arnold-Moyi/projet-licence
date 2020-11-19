from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import UsersForm, EditProfileForm, review_livre, review_memoire, review_article
from blog.models import Utilisateur, Memoire, ArticleJournaux, Review, Review_livre, Review_memoire, Review_article
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Livre


def home(request):
    return render(request, 'blog/home.html')


def Login(request):
    return render(request, 'blog/login.html')


def About(request):
    return render(request, 'blog/about.html')


@login_required
def Dashboard(request):
    return render(request, 'blog/accueil_user.html')


def Formulaire(request):
    context = {}
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            mail = form.cleaned_data['mail']

            user = User.objects.filter(username=username)
            # voir l'existance d'username
            if not user.exists():
                user = User.objects.create_user(
                    username, mail, password)

                nom = form.cleaned_data['nom']
                prenom = form.cleaned_data['prenom']
                date_de_naissance = form.cleaned_data['date_de_naissance']

                Utilisateur.objects.create(
                    username=username,
                    nom=nom,
                    prenom=prenom,
                    date_de_naissance=date_de_naissance,
                )

                return render(request, 'blog/login.html')
            else:
                # compte existant affiche un message
                messages.error(request, 'compte existant, '
                                        'changer votre username')

    form = UsersForm()
    context['form'] = form
    return render(request, 'blog/formulaire.html', context)


def Connect(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if not user:
            # afficher message username ou password incorrect

            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

        else:
            login(request, user)
            return redirect(reverse('accueil'))

    return render(request, 'blog/login.html')


def SeDeconnecter(request):
    logout(request)
    return redirect(reverse('login'))


@login_required()
def Change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, 'votre mot de passe a été mis à jour avec succès!')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'blog/pwd.html', {
        'form': form
    })


@login_required()
def EditProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'la mise à jour de vos informations est effectuée!')
            return redirect('edit_profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {
        'form': form
    })


def liste_livre(request):
    livres = Livre.objects.all()
    return render(request, 'blog/Liste_livre.html', {'livres': livres})


def info(request):
    livres = Livre.objects.all()

    return render(request, 'blog/informatique.html', {'livres': livres})


def Math(request):
    livres = Livre.objects.all()
    return render(request, 'blog/Mathematique.html', {'livres': livres})


def Bio(request):
    livres = Livre.objects.all()
    return render(request, 'blog/Biologie.html', {'livres': livres})


def Licence(request):
    memoires = Memoire.objects.all()
    return render(request, 'blog/Licence.html', {'memoires': memoires})


def Master(request):
    memoires = Memoire.objects.all()
    return render(request, 'blog/Master.html', {'memoires': memoires})


def Doctorat(request):
    memoires = Memoire.objects.all()
    return render(request, 'blog/Doctorat.html', {'memoires': memoires})


def Foot(request):
    articles = ArticleJournaux.objects.all()
    return render(request, 'blog/Football.html', {'articles': articles})


def Basket(request):
    articles = ArticleJournaux.objects.all()
    return render(request, 'blog/Basketball.html', {'articles': articles})


def Judo(request):
    articles = ArticleJournaux.objects.all()
    return render(request, 'blog/Judo.html', {'articles': articles})


def recherche(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            livres = Livre.objects.filter(Q(intitulé__icontains=search))
            memoires = Memoire.objects.filter(Q(intitulé__icontains=search))
            articles = ArticleJournaux.objects.filter(Q(intitulé__icontains=search))
            if livres or memoires or articles:
                return render(request, 'blog/Recherche.html',
                              {'livres': livres, 'memoires': memoires, 'articles': articles})
            else:
                return render(request, 'blog/introuvable.html')

    return render(request, 'blog/Recherche.html')


def reviews_livre(request):
    form = review_livre()
    if request.method == 'POST':
        # forms = Reviews(request.POST)
        form = review_livre(request.POST)
        # utilisateurs = forms.cleaned_data['utilisateur']
        if form.is_valid():
            form.save()
            # messages.success(request, 'votre commentaire a été enregistré avec succès!')
            return render(request, 'blog/accueil_user.html')

    context = {'form': form}
    return render(request, 'blog/Review.html', context)


def reviews_memoire(request):
    form = review_memoire()
    if request.method == 'POST':
        form = review_memoire(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'votre commentaire a été enregistré avec succès!')
            return render(request, 'blog/accueil_user.html')

    context = {'form': form}
    return render(request, 'blog/Review.html', {'form': form})


def reviews_article(request):
    form = review_article()
    if request.method == 'POST':

        form = review_article(request.POST)

        if form.is_valid():
            form.save()
            # messages.success(request, 'votre commentaire a été enregistré avec succès!')
            return render(request, 'blog/accueil_user.html')

    context = {'form': form}
    return render(request, 'blog/Review.html', {'form': form})


def Avis_livre(request):
    avis = Review_livre.objects.all()
    return render(request, 'blog/Avis_livre.html', {'avis': avis})


def Avis_memoire(request):
    avis = Review_memoire.objects.all()
    return render(request, 'blog/Avis_memoire.html', {'avis': avis})


def Avis_article(request):
    avis = Review_article.objects.all()
    return render(request, 'blog/Avis_article.html', {'avis': avis})
