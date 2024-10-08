# Generated by Django 5.0.7 on 2024-08-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_company_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='founder',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='مدیر عامل'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='لینک سایت'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='شماره تماس'),
        ),
    ]
