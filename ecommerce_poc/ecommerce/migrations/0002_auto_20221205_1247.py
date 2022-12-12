# Generated by Django 3.2 on 2022-12-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generator',
            name='generator_fuel_type',
            field=models.CharField(choices=[('gasoline', 'gasoline'), ('LP', 'LP'), ('Dual Fuel', 'Dual Fuel'), ('Diesel', 'Diesel'), ('Tri-Fuel', 'Tri-Fuel')], max_length=64),
        ),
        migrations.AlterField(
            model_name='generator',
            name='product_category',
            field=models.CharField(choices=[('generator', 'generator'), ('wood_stove', 'wood_stove'), ('pellet_stove', 'pellet_stove'), ('power_equipment', 'power_equipment'), ('mobility_scooter', 'mobility_scooter'), ('water_heater', 'water_heater'), ('electronic', 'electronic'), ('air_control', 'air_control')], max_length=128),
        ),
    ]
