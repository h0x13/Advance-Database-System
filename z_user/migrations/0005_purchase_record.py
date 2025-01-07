# Generated by Django 5.1.4 on 2025-01-07 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_admin', '0005_coffee'),
        ('z_user', '0004_user_account_first_name_user_account_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_admin.coffee')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_user.user_account')),
            ],
            options={
                'verbose_name': 'Purchase Record',
                'verbose_name_plural': 'Purchase Records',
            },
        ),
    ]
