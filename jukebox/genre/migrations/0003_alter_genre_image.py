# Generated by Django 3.2.12 on 2022-04-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_genre_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(default='/static/img/placeholder.png', upload_to='images/genres/'),
        ),
    ]
