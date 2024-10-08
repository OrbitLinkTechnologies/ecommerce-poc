# Generated by Django 3.2 on 2023-01-07 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0025_productreview_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='review_created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productreview',
            name='review_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
