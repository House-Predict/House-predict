# Generated by Django 2.0.7 on 2021-01-21 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210122_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 21, 19, 6, 47, 54923, tzinfo=utc)),
        ),
    ]