# Generated by Django 5.0.7 on 2024-08-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_slider_subtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='subtext',
            field=models.CharField(max_length=150, verbose_name='سابتکست'),
        ),
    ]
