# Generated by Django 2.2 on 2021-03-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impressum_app', '0002_auto_20210325_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='impressummodel',
            options={'ordering': ('ordering',), 'verbose_name': 'Impressum oder AGB', 'verbose_name_plural': "Impressum und AGB's "},
        ),
        migrations.AddField(
            model_name='impressummodel',
            name='ordering',
            field=models.IntegerField(default=1, verbose_name='Reihenfolge'),
        ),
    ]
