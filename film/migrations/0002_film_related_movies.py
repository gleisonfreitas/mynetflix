# Generated by Django 4.2.8 on 2023-12-31 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='related_movies',
            field=models.ManyToManyField(to='film.film'),
        ),
    ]
