# Generated by Django 2.2.19 on 2022-03-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220307_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
