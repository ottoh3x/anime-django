# Generated by Django 3.0.8 on 2021-03-11 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0017_auto_20210311_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='category',
        ),
        migrations.AddField(
            model_name='anime',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.AnimeCategory'),
        ),
    ]
