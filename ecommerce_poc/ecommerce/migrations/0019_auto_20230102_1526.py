# Generated by Django 3.2 on 2023-01-02 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_alter_customer_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
