# Generated by Django 3.2 on 2021-05-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_vendorx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
