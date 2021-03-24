# Generated by Django 2.2 on 2021-03-18 14:25

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0018_auto_20210318_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('bild', '800x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
