# Generated by Django 3.2 on 2023-01-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0030_auto_20230107_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='stripe_checkout_session_id',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delivery',
            name='stripe_invoice_id',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]
