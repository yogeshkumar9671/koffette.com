# Generated by Django 4.0.2 on 2022-02-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TW', 'Top Wear'), ('BT', 'Bottom Wear'), ('S', 'Shoes'), ('BEA', 'Beauty Product'), ('CO', 'Coffee'), ('GRO', 'Grocery'), ('Acce', 'Accessories')], max_length=5),
        ),
    ]
