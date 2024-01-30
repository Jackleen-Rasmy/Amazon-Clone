# Generated by Django 4.2 on 2024-01-30 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_profile_contactnumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactnumbers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contact', to=settings.AUTH_USER_MODEL),
        ),
    ]