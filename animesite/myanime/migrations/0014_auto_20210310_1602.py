# Generated by Django 3.0.8 on 2021-03-10 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0013_auto_20210309_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='slug',
            new_name='slugy',
        ),
    ]
