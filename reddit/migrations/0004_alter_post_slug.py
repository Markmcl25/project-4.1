# Generated by Django 5.1.3 on 2024-11-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0003_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]