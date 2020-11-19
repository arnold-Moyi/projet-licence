from django.contrib.auth.models import User
from django.db import models


class Utilisateur(models.Model):
    username = models.CharField(User, max_length=100, default=None)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField(max_length=10)

    def __str__(self):
        return self.username


class Document(models.Model):
    intitulé = models.CharField(max_length=100, default="")
    nomAuteur = models.CharField(max_length=100, default="")
    maison_edition = models.CharField(max_length=100, default="")
    annéeEdition = models.DateField(max_length=100, default="")
    nombrePages = models.IntegerField()
    type = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.utilisateur)

    class Meta:
        abstract = True


class Livre(Document):
    Nbre_tome = models.IntegerField(default=None)
    livre = models.FileField(upload_to='livre', default="")

    def __str__(self):
        return self.intitulé


class Memoire(Document):
    nombreChapitre = models.IntegerField()
    memoire = models.FileField(upload_to='memoire', default="")

    def __str__(self):
        return self.intitulé


class ArticleJournaux(Document):
    prix = models.IntegerField()
    article = models.FileField(upload_to='article', default=None)

    def __str__(self):
        return self.intitulé


class Review(models.Model):
    critique = models.TextField(max_length=500, null=True)

    # utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.critique


class Review_livre(Review):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.critique


class Review_memoire(Review):
    memoire = models.ForeignKey(Memoire, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.critique


class Review_article(Review):
    article = models.ForeignKey(ArticleJournaux, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.critique
