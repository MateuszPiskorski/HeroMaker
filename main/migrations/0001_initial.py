# Generated by Django 4.1.2 on 2022-10-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('first_level_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fellowship', models.PositiveSmallIntegerField()),
                ('willpower', models.PositiveSmallIntegerField()),
                ('intelligence', models.PositiveSmallIntegerField()),
                ('dexterity', models.PositiveSmallIntegerField()),
                ('agility', models.PositiveSmallIntegerField()),
                ('initiative', models.PositiveSmallIntegerField()),
                ('toughness', models.PositiveSmallIntegerField()),
                ('strength', models.PositiveSmallIntegerField()),
                ('ballistic_skill', models.PositiveSmallIntegerField()),
                ('weapon_skill', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1024)),
                ('rule_set', models.CharField(default='classic', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('careers', models.ManyToManyField(to='main.career')),
            ],
        ),
    ]
