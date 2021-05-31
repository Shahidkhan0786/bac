# Generated by Django 3.2 on 2021-05-16 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_product_case_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cpu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cpu'),
        ),
        migrations.AddField(
            model_name='product',
            name='graphic_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.graphic_card'),
        ),
        migrations.AddField(
            model_name='product',
            name='mobo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.motherboard'),
        ),
        migrations.AddField(
            model_name='product',
            name='psu_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.smps'),
        ),
        migrations.AddField(
            model_name='product',
            name='ram_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.ram'),
        ),
        migrations.AddField(
            model_name='product',
            name='storage_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.storage'),
        ),
    ]