# Generated by Django 5.0.6 on 2024-10-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0027_rename_diy_doityourself_alter_comparisons_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doityourself',
            name='question1_answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
