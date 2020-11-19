from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from blog.models import Livre, Review, Review_livre, Review_memoire, Review_article


class UsersForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'type': 'text', 'id': 'username', 'placeholder': 'username',
                   'aria-describedby': 'basic-addon1', 'required': 'required'}))
    nom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'nom', 'placeholder': 'nom',
                                      'aria-describedby': 'basic-addon1', 'required': 'required'}))
    prenom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'prenom', 'placeholder': 'Prénom',
                                      'aria-describedby': 'basic-addon1', 'required': 'required'}))

    date_de_naissance = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'dateNaissance',
                                      'placeholder': 'Date de naissance ex: 11/25/2020',
                                      'aria-describedby': 'basic-addon1', 'required': 'required'}))
    mail = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'id': 'mail', 'placeholder': 'Email',
                                       'aria-describedby': 'basic-addon1', 'required': 'required'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'id': 'motDePasse', 'placeholder': 'Mot de passe',
                   'aria-describedby': 'basic-addon1', 'required': 'required'}))


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class livre_form(forms.ModelForm):
    class Meta:
        model = Livre
        fields = (
            'intitulé',
            'nomAuteur',
            'livre',
            'maison_edition',
            'annéeEdition',
            'nombrePages',
            'type',
        )


class review_livre(ModelForm):
    class Meta:
        model = Review_livre
        fields = ('critique',
                  'livre',

                  )


class review_memoire(ModelForm):
    class Meta:
        model = Review_memoire
        fields = ('critique',
                  'memoire',)


class review_article(ModelForm):
    class Meta:
        model = Review_article
        fields = ('critique',
                  'article',
                  )
