# Generated by Django 3.0.6 on 2020-05-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('composer', models.CharField(blank=True, max_length=64, null=True)),
                ('lyricist', models.CharField(blank=True, max_length=64, null=True)),
                ('singer', models.CharField(blank=True, max_length=64, null=True)),
                ('published_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Base Song',
                'verbose_name_plural': 'Base Songs',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('is_covered', models.BooleanField(default=False)),
                ('base_song', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='songs.BaseSong')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
