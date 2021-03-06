# Generated by Django 4.0.1 on 2022-02-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('product_discription', models.CharField(max_length=500)),
                ('brand_name', models.CharField(max_length=50)),
                ('product_title', models.CharField(max_length=200)),
                ('selling_price', models.IntegerField()),
                ('actual_price', models.IntegerField()),
                ('off_upto', models.IntegerField()),
                ('img', models.ImageField(upload_to='productImg')),
                ('img2', models.ImageField(upload_to='productImg')),
                ('img3', models.ImageField(upload_to='productImg')),
                ('img4', models.ImageField(upload_to='productImg')),
            ],
        ),
    ]
