# Generated by Django 4.0.1 on 2022-02-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_description_alter_customer_pincode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discounted_price',
            new_name='actual_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='brand_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='product_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=-1.0, upload_to='productImg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, upload_to='productImg'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, upload_to='productImg'),
        ),
        migrations.AddField(
            model_name='product',
            name='img4',
            field=models.ImageField(blank=True, upload_to='productImg'),
        ),
        migrations.AddField(
            model_name='product',
            name='off_upto',
            field=models.IntegerField(default=-1.0),
            preserve_default=False,
        ),
    ]