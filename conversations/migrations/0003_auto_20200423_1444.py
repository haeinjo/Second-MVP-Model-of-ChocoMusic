# Generated by Django 3.0.5 on 2020-04-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20200327_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
