# Generated by Django 3.2.12 on 2022-04-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0004_alter_genre_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]