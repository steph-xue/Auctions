# Generated by Django 5.0.4 on 2024-05-03 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_listing_category_listing_current_highest_bid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='listing_item',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='current_highest_bid',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='title',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
    ]
