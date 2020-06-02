# Generated by Django 3.0.6 on 2020-06-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('recruitments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruits', to='teams.Team'),
        ),
    ]
