# Generated by Django 5.0.6 on 2024-10-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0020_song_related_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_clip_file',
            field=models.FileField(blank=True, null=True, upload_to='static/carnatic_music'),
        ),
    ]
