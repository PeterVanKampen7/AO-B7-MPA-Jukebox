# Generated by Django 3.2.12 on 2022-04-11 11:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0004_alter_genre_image'),
        ('artist', '0004_alter_artist_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('views', models.IntegerField(default=0, editable=False)),
                ('dateAdded', models.DateField(default=datetime.date(2022, 4, 11), editable=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
                ('genre', models.ManyToManyField(to='genre.Genre')),
            ],
        ),
    ]
