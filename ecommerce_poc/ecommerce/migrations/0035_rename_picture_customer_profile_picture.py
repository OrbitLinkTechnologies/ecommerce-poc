# Generated by Django 3.2 on 2023-05-25 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0034_customer_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='picture',
            new_name='profile_picture',
        ),
    ]
