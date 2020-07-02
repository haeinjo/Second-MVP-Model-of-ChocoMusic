# Generated by Django 3.0.6 on 2020-06-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200625_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login_methods',
        ),
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('google', 'Google'), ('kakao', 'Kakao'), ('email', 'Email')], default='', max_length=16),
        ),
    ]
