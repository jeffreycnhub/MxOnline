# Generated by Django 2.2 on 2021-01-03 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_auto_20210103_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercourse',
            old_name='coursce',
            new_name='course',
        ),
    ]
