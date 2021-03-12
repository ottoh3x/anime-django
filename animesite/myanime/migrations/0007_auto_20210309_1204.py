# Generated by Django 3.0.8 on 2021-03-09 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0006_auto_20210308_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(help_text='Auto-generated from Title.', unique=True)),
                ('episode', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(help_text='Auto-generated from Title.', unique=True)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=models.SlugField(help_text='Auto-generated from Title.', unique=True),
        ),
        migrations.DeleteModel(
            name='AnimeWatch',
        ),
        migrations.AddField(
            model_name='episode',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.Anime'),
        ),
    ]
