# Generated by Django 5.0.6 on 2024-10-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0021_song_song_clip_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Varnam',
            fields=[
                ('varnam_id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('posted_week', models.IntegerField(null=True)),
                ('posted_date', models.DateField(null=True)),
            ],
        ),
    ]
