# Generated by Django 2.2 on 2021-03-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titel')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Eine Beschreibung auf die Homeseite',
                'verbose_name_plural': 'Die Beschreibungen auf die Homeseite ',
            },
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titel')),
                ('title_description', models.TextField(blank=True, null=True, verbose_name='Titels Zusatz')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Eine Beschreibung mit den Bildern auf die Homeseite',
                'verbose_name_plural': 'Die Beschreibungen mit den Bildern auf die Homeseite ',
            },
        ),
        migrations.CreateModel(
            name='HomeText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titel')),
                ('description', models.TextField(blank=True, null=True, verbose_name='text')),
            ],
            options={
                'verbose_name': 'Der erste Text auf Die Homseite',
                'verbose_name_plural': 'Der erste Text auf Die Homseite',
            },
        ),
    ]
