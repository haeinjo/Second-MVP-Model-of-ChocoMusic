# Generated by Django 3.0.6 on 2020-06-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200606_1807'),
        ('contents', '0004_auto_20200611_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='genres',
        ),
        migrations.AddField(
            model_name='content',
            name='genres',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='core.Genre'),
        ),
    ]
