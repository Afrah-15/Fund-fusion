# Generated by Django 4.2.5 on 2024-04-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepayment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Orderid', models.CharField(default='', max_length=100)),
                ('Amount', models.CharField(default='', max_length=100)),
                ('Time', models.CharField(default='', max_length=100)),
                ('Date', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
