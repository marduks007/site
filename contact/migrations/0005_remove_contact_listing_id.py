# Generated by Django 3.2.5 on 2021-08-12 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20210812_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='listing_id',
        ),
    ]
