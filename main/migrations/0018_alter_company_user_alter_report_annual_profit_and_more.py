# Generated by Django 5.0.7 on 2024-08-07 18:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_report_company_report_current_expense_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='annual_profit',
            field=models.CharField(max_length=50, verbose_name='سود سالیانه'),
        ),
        migrations.AlterField(
            model_name='report',
            name='budget',
            field=models.CharField(max_length=50, verbose_name='بودجه اولیه'),
        ),
        migrations.AlterField(
            model_name='report',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcompany', to='main.company', verbose_name='شرکت'),
        ),
        migrations.AlterField(
            model_name='report',
            name='current_expense',
            field=models.CharField(max_length=50, verbose_name='هزینه جاری'),
        ),
        migrations.AlterField(
            model_name='report',
            name='expected_budget',
            field=models.CharField(max_length=50, verbose_name='پیش بینی بودجه'),
        ),
        migrations.AlterField(
            model_name='report',
            name='staff_number',
            field=models.CharField(max_length=50, verbose_name='تعداد پرسنل'),
        ),
        migrations.AlterField(
            model_name='report',
            name='year_analysis',
            field=models.TextField(verbose_name='عملکرد امسال'),
        ),
    ]
