# Generated by Django 2.2 on 2021-03-16 18:52

from django.db import migrations, models
import django.db.models.deletion
import smartfields.fields
import smartfields.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategorie_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': ' Kategorien',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('bild', smartfields.fields.ImageField(blank=True, null=True, upload_to='photo/%m/')),
                ('bild_png', smartfields.fields.ImageField(blank=True, null=True, upload_to='')),
                ('bild_webp', smartfields.fields.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('kategorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_app.Kategorien')),
            ],
            options={
                'verbose_name': 'Work zum Portfolio',
                'verbose_name_plural': 'Works zum Portfolio',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
    ]