# Generated by Django 4.2 on 2024-01-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_cartdetails_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]