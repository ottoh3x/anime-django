# Generated by Django 3.0.8 on 2021-03-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myanime', '0010_auto_20210309_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
