# Generated by Django 4.2.5 on 2024-04-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepayment', '0003_history_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Status',
            field=models.CharField(default='', max_length=100),
        ),
    ]
