# Generated by Django 2.2 on 2021-03-16 14:59

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0004_auto_20210316_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='icon',
        ),
        migrations.AddField(
            model_name='services',
            name='bild',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to='media/photo/%m/'),
        ),
        migrations.AddField(
            model_name='services',
            name='bild_png',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='services',
            name='bild_webp',
            field=smartfields.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]