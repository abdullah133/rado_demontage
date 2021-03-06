# Generated by Django 2.2 on 2021-03-18 21:18

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0007_teammodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammodel',
            name='bild',
        ),
        migrations.AddField(
            model_name='teammodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='über_uns_bilder/%m/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('photo', '400x465', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
