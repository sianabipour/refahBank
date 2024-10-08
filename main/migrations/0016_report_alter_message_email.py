# Generated by Django 5.0.7 on 2024-08-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_company_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annual_profit', models.CharField(max_length=50, verbose_name='سود سالیانه')),
                ('budget', models.CharField(max_length=50, verbose_name='بودجه اولیه')),
                ('staff_number', models.CharField(max_length=50, verbose_name='تعداد پرسنل')),
            ],
            options={
                'verbose_name': 'گزارش',
                'verbose_name_plural': 'گزارشها',
            },
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
    ]
