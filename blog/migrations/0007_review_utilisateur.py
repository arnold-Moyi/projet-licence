# Generated by Django 3.0.8 on 2020-07-18 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_review_livre_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='utilisateur',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Utilisateur'),
        ),
    ]
