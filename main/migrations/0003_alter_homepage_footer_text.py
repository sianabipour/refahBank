# Generated by Django 5.0.7 on 2024-07-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_homepage_alter_company_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='footer_text',
            field=models.TextField(verbose_name='متن فوتر'),
        ),
    ]
