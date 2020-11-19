from django.contrib import admin

from .models import Utilisateur, Livre, ArticleJournaux, Memoire, Review_livre, Review_memoire, Review_article

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Livre)
admin.site.register(Memoire)
admin.site.register(ArticleJournaux)
admin.site.register(Review_livre)
admin.site.register(Review_memoire)
admin.site.register(Review_article)




