# Generated by Django 5.0.7 on 2024-08-07 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_report_alter_message_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subcompany', to='main.company', verbose_name='شرکت'),
        ),
        migrations.AddField(
            model_name='report',
            name='current_expense',
            field=models.CharField(default='متن خود را وارد کنید', max_length=50, verbose_name='هزینه جاری'),
        ),
        migrations.AddField(
            model_name='report',
            name='expected_budget',
            field=models.CharField(default='متن خود را وارد کنید', max_length=50, verbose_name='پیش بینی بودجه'),
        ),
        migrations.AddField(
            model_name='report',
            name='year_analysis',
            field=models.TextField(default='متن خود را وارد کنید', verbose_name='عملکرد امسال'),
        ),
        migrations.AlterField(
            model_name='report',
            name='annual_profit',
            field=models.CharField(default='متن خود را وارد کنید', max_length=50, verbose_name='سود سالیانه'),
        ),
        migrations.AlterField(
            model_name='report',
            name='budget',
            field=models.CharField(default='متن خود را وارد کنید', max_length=50, verbose_name='بودجه اولیه'),
        ),
        migrations.AlterField(
            model_name='report',
            name='staff_number',
            field=models.CharField(default='متن خود را وارد کنید', max_length=50, verbose_name='تعداد پرسنل'),
        ),
    ]
