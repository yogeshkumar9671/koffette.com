# Generated by Django 4.0.2 on 2022-02-20 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='off_upto',
        ),
    ]