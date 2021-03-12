# Generated by Django 3.0.8 on 2021-03-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0012_auto_20210309_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='episode',
        ),
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='animecategory',
            name='category',
            field=models.CharField(choices=[('genre_choice1', 'Action'), ('genre_choice2', 'Adventure'), ('genre_choice3', 'Comedy'), ('genre_choice4', 'Drama'), ('genre_choice5', 'Fantasy'), ('genre_choice6', 'Horror'), ('genre_choice7', 'Martial Arts'), ('genre_choice8', 'Mystery'), ('genre_choice9', 'Super Power'), ('genre_choice10', 'Supernatural')], max_length=200),
        ),
    ]
