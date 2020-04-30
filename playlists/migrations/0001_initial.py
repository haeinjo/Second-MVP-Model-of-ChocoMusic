# Generated by Django 3.0.5 on 2020-04-30 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0007_auto_20200427_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=32)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paly_lists', to='playlists.ListCategory')),
                ('songs', models.ManyToManyField(related_name='play_lists', to='songs.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='play_lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
