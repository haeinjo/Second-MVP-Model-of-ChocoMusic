# Generated by Django 3.0.6 on 2020-06-06 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_borough_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borough',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boroughs', to='core.City'),
        ),
    ]
