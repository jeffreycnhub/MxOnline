# Generated by Django 2.2 on 2021-01-03 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecomments',
            old_name='coursce',
            new_name='course',
        ),
    ]
