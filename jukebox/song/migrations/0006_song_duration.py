# Generated by Django 4.0.3 on 2022-05-09 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0005_remove_song_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]