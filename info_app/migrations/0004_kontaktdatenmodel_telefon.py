# Generated by Django 2.2 on 2021-03-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0003_remove_kontaktdatenmodel_erreichbarkeit'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontaktdatenmodel',
            name='telefon',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Telefon Nr.'),
        ),
    ]