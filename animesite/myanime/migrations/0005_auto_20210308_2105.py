# Generated by Django 3.0.8 on 2021-03-08 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0004_auto_20210308_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='animewatch',
            old_name='name',
            new_name='title',
        ),
    ]
