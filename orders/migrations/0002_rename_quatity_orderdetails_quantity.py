# Generated by Django 4.2 on 2024-01-11 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
