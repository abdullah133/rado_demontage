# Generated by Django 2.2 on 2021-03-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0019_auto_20210318_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=40, null=True),
        ),
    ]
