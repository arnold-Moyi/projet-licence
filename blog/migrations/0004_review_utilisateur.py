# Generated by Django 3.0.8 on 2020-07-15 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200715_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='utilisateur',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Utilisateur'),
        ),
    ]
