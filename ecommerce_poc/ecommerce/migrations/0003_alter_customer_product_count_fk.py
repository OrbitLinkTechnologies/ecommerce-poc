# Generated by Django 3.2 on 2022-12-26 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_homedecor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='product_count_FK',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.baseproduct'),
        ),
    ]
