# Generated by Django 2.2 on 2021-03-09 21:48

from django.db import migrations, models
import smartfields.fields
import smartfields.models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_homeband'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bild', smartfields.fields.ImageField(blank=True, null=True, upload_to='photo/%m/')),
                ('bild_png', smartfields.fields.ImageField(blank=True, null=True, upload_to='')),
                ('bild_webp', smartfields.fields.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Das Foto auf die Homseite',
                'verbose_name_plural': 'Das Foto Auf die Homeseite',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
    ]