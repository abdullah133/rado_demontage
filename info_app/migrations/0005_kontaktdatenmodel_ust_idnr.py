# Generated by Django 2.2 on 2021-03-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0004_kontaktdatenmodel_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontaktdatenmodel',
            name='ust_idnr',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='UST-IDNr'),
        ),
    ]
