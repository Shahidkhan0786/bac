# Generated by Django 3.2 on 2021-05-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_ram_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphic_card',
            name='version',
            field=models.CharField(choices=[('version 1', 'version 1'), ('version 2', 'version 2'), ('version 3', 'version 3')], default='version 1', max_length=250),
        ),
    ]
