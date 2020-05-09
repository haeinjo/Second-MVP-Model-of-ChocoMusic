# Generated by Django 3.0.6 on 2020-05-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('active_region', models.CharField(max_length=256)),
                ('avatar', models.ImageField(upload_to='')),
                ('is_solo', models.BooleanField()),
                ('genres', models.ManyToManyField(to='core.Genre')),
                ('positions', models.ManyToManyField(to='core.Position')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
