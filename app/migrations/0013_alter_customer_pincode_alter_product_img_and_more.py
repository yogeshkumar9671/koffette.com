# Generated by Django 4.0.2 on 2022-02-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_product_off_upto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='productImg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='productImg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='productImg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='productImg'),
        ),
    ]
