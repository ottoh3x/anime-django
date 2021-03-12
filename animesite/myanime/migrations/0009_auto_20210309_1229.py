# Generated by Django 3.0.8 on 2021-03-09 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0008_auto_20210309_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('DRAMA', 'DRAMA'), ('ROMANCE', 'ROMANCE'), ('ACTION', 'ACTION'), ('SUPERPOWER', 'SUPERPOWER')], max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='season',
            new_name='saison',
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.Anime'),
        ),
        migrations.AlterField(
            model_name='season',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.Anime'),
        ),
        migrations.AddField(
            model_name='season',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.AnimeCategory'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.AnimeCategory'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myanime.AnimeCategory'),
        ),
    ]
