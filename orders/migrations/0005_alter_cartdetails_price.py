# Generated by Django 4.2 on 2024-01-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_cartdetails_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetails',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]