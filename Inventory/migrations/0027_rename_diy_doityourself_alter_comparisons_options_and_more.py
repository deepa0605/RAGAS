# Generated by Django 5.0.6 on 2024-10-16 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0026_diy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diy',
            new_name='DoItYourself',
        ),
        migrations.AlterModelOptions(
            name='comparisons',
            options={'verbose_name': 'Comparisons', 'verbose_name_plural': 'Comparisons'},
        ),
        migrations.AlterModelOptions(
            name='doityourself',
            options={'verbose_name': 'Do it yourself', 'verbose_name_plural': 'Do it yourself'},
        ),
    ]
