# Generated by Django 5.0.1 on 2024-02-05 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='contry',
            new_name='country',
        ),
    ]
