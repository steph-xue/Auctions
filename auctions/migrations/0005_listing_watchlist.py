# Generated by Django 5.0.4 on 2024-05-03 03:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
