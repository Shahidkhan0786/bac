# Generated by Django 3.2 on 2021-06-21 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_alter_build_pc_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build_pc',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildpc', to=settings.AUTH_USER_MODEL),
        ),
    ]