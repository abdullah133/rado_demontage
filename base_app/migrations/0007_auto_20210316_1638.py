# Generated by Django 2.2 on 2021-03-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0006_delete_homeservice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeBand',
        ),
        migrations.DeleteModel(
            name='HomeDescription',
        ),
        migrations.DeleteModel(
            name='HomeImg',
        ),
        migrations.DeleteModel(
            name='HomeText',
        ),
    ]
