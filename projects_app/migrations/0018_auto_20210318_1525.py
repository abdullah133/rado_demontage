# Generated by Django 2.2 on 2021-03-18 14:25

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0017_auto_20210318_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='bild_png',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='bild_webp',
        ),
        migrations.AlterField(
            model_name='projects',
            name='bild',
            field=models.ImageField(blank=True, upload_to='projects/%m/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('Bild', '800x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
