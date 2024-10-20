# Generated by Django 5.0.6 on 2024-10-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0018_song_composer_song_tala'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='related_ragas',
            field=models.ManyToManyField(blank=True, related_name='songs', to='Inventory.raga'),
        ),
        migrations.AlterField(
            model_name='raga',
            name='related_songs',
            field=models.ManyToManyField(blank=True, related_name='ragas', to='Inventory.song'),
        ),
    ]
