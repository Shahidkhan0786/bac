# Generated by Django 3.2 on 2021-05-15 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20210515_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='graphic_card',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='ram',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='smps',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AddField(
            model_name='storage',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, choices=[('mobo', 'mobo'), ('ram', 'ram'), ('processor', 'processor'), ('graphicCard', 'graphic-card'), ('storage', 'storage'), ('powersupply', 'powersupply')], default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]