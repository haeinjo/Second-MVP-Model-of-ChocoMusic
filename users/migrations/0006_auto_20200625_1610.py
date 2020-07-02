# Generated by Django 3.0.6 on 2020-06-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_loginmethod'),
        ('users', '0005_auto_20200609_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login_method',
        ),
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.ManyToManyField(related_name='users', to='core.LoginMethod'),
        ),
    ]
