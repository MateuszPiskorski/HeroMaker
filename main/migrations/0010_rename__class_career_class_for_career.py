# Generated by Django 4.1.2 on 2022-10-18 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_career_short_description_class_short_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='_class',
            new_name='class_for_career',
        ),
    ]
