# Generated by Django 3.1.3 on 2020-11-24 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20201119_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='title'),
        ),
    ]