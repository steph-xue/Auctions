# Generated by Django 5.0.4 on 2024-05-02 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_user_listing_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
