# Generated by Django 3.0.5 on 2020-04-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_auto_20200427_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basesong',
            name='composer',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='basesong',
            name='lyricist',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='basesong',
            name='singer',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
