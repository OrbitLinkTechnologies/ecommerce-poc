# Generated by Django 3.2 on 2022-12-27 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20221226_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseproduct',
            name='product_count_in_user_cart',
        ),
        migrations.RemoveField(
            model_name='baseproduct',
            name='product_in_user_cart',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='product_count_FK',
        ),
    ]
