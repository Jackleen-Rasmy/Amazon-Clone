# Generated by Django 4.2 on 2023-12-10 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, verbose_name='rate'),
        ),
    ]