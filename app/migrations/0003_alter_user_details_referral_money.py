# Generated by Django 4.1.3 on 2023-03-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_details_referral_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='referral_money',
            field=models.BigIntegerField(default=0),
        ),
    ]
