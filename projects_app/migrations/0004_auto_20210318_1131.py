# Generated by Django 2.2 on 2021-03-18 10:31

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0003_projects_cropping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='bild',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to='projects/%m/'),
        ),
    ]
