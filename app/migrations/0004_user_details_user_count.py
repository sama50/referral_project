# Generated by Django 4.1.3 on 2023-03-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_details_referral_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='user_count',
            field=models.BigIntegerField(default=0),
        ),
    ]
