# Generated by Django 3.0.8 on 2021-03-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
