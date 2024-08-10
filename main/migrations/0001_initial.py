# Generated by Django 5.0.7 on 2024-07-31 16:39

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام سازمان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='company', verbose_name='تصویر')),
                ('subs', models.ManyToManyField(blank=True, to='main.company', verbose_name='زیر مجموعه ها')),
            ],
            options={
                'verbose_name': 'سازمان',
            },
        ),
    ]
