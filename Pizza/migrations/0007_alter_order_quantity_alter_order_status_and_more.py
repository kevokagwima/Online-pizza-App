# Generated by Django 4.1.1 on 2022-09-27 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0006_order_user_alter_order_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 14, 43, 4, 310649)),
        ),
    ]
