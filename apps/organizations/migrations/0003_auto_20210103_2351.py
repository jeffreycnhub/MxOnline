# Generated by Django 2.2 on 2021-01-03 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20210103_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='work_compang',
            new_name='work_company',
        ),
    ]
