# Generated by Django 3.0.6 on 2020-06-14 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_auto_20200614_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='genres',
            new_name='genre',
        ),
    ]
