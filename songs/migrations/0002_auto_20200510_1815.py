# Generated by Django 3.0.6 on 2020-05-10 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('songs', '0001_initial'),
        ('projects', '0002_auto_20200510_1815'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='composer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='composed_songs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='core.Genre'),
        ),
        migrations.AddField(
            model_name='song',
            name='lyricist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='lyric_songs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='song',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='role',
            name='position',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='core.Position'),
        ),
        migrations.AddField(
            model_name='role',
            name='song',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='songs.Song'),
        ),
        migrations.AddField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL),
        ),
    ]
