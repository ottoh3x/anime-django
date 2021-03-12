# Generated by Django 3.0.8 on 2021-03-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(choices=[('DRAMA', 'DRAMA'), ('ROMANCE', 'ROMANCE'), ('ACTION', 'ACTION'), ('SUPERPOWER', 'SUPERPOWER')], max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
