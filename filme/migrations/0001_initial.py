# Generated by Django 5.0 on 2023-12-14 21:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_film')),
                ('description', models.TextField(max_length=1000)),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('DRAMA', 'Drama'), ('COMEDY', 'Comedy')], max_length=15)),
                ('visualization', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]