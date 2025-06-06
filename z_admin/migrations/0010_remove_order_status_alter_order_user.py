# Generated by Django 5.1.4 on 2025-01-09 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_admin', '0009_alter_order_options_order_status'),
        ('z_user', '0006_alter_purchase_record_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_user.user_account'),
        ),
    ]
