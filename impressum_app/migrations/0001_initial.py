# Generated by Django 2.2 on 2021-03-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpressumModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titel')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Beschreibung und Bild',
                'verbose_name_plural': 'Beschreibungen und Bilder ',
            },
        ),
    ]
