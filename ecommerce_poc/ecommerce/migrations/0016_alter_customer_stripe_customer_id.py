# Generated by Django 3.2 on 2022-12-29 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_customer_stripe_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
