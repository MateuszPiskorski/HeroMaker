# Generated by Django 4.1.2 on 2022-10-07 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_species_careers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='species',
            old_name='careers',
            new_name='disallowed_careers',
        ),
    ]