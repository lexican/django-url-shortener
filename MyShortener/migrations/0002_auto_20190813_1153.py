# Generated by Django 2.2.4 on 2019-08-13 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyShortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='short_urls',
            old_name='long_urls',
            new_name='long_url',
        ),
    ]
