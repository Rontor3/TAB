# Generated by Django 3.1.7 on 2021-04-01 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Place', '0002_auto_20210402_0018'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activities',
            new_name='Acti',
        ),
        migrations.RenameField(
            model_name='location_destination',
            old_name='location_destination',
            new_name='ld',
        ),
    ]
