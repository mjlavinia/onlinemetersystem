# Generated by Django 4.1.7 on 2023-04-23 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0015_clientinfo_remarks_alter_meterlog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 23, 22, 26, 59, 690473, tzinfo=datetime.timezone.utc)),
        ),
    ]