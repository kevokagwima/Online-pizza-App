# Generated by Django 4.1.1 on 2022-09-27 11:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pizza', '0005_alter_user_profile_date_created_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 14, 38, 23, 967154)),
        ),
    ]
