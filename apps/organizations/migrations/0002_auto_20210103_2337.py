# Generated by Django 2.2 on 2021-01-03 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '城市名', 'verbose_name_plural': '城市名'},
        ),
    ]
