# Generated by Django 3.0.6 on 2020-06-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200606_1807'),
        ('users', '0004_auto_20200609_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alias',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='borough',
            field=models.ManyToManyField(blank=True, related_name='users', to='core.Borough'),
        ),
    ]
