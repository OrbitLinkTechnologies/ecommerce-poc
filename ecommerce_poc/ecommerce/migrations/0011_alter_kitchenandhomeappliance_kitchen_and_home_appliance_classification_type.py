# Generated by Django 3.2 on 2022-12-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_kitchenandhomeappliance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchenandhomeappliance',
            name='kitchen_and_home_appliance_classification_type',
            field=models.CharField(choices=[('Air Fryer', 'Air Fryer'), ('Oven', 'Oven'), ('Toaster', 'Toaster'), ('Microwave', 'Microwave'), ('Coffee Maker', 'Coffee Maker'), ('Air Conditioner', 'Air Conditioner'), ('Dishwasher', 'Dishwasher'), ('Clothes Washer', 'Clothes Washer'), ('Clothes Dryer', 'Clothes Dryer'), ('Water Heater', 'Water Heater')], max_length=64),
        ),
    ]
