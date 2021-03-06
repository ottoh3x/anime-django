# Generated by Django 3.0.8 on 2021-03-09 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0011_auto_20210309_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='title',
            new_name='title_en',
        ),
        migrations.AddField(
            model_name='anime',
            name='title_jp',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Series Title (Japan)'),
        ),
        migrations.AddField(
            model_name='episode',
            name='anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.Anime'),
        ),
        migrations.AddField(
            model_name='episode',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Episode Title'),
        ),
        migrations.AddField(
            model_name='episode',
            name='number',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Episode Number'),
        ),
        migrations.AlterField(
            model_name='season',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together={('anime', 'number')},
        ),
        migrations.RemoveField(
            model_name='episode',
            name='title',
        ),
    ]
