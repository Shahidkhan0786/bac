# Generated by Django 3.2 on 2021-05-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_graphic_card_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphic_card',
            name='recommended_watt',
            field=models.CharField(default='', max_length=250),
        ),
    ]
