# Generated by Django 2.2 on 2021-03-16 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0009_projects_kategorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='url',
        ),
    ]
