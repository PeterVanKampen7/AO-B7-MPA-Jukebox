# Generated by Django 3.2.12 on 2022-04-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0006_remove_artist_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='popularity',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
