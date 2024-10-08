# Generated by Django 3.2 on 2022-12-24 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_category', models.CharField(choices=[('generator', 'generator'), ('wood_stove', 'wood_stove'), ('pellet_stove', 'pellet_stove'), ('power_equipment', 'power_equipment'), ('mobility_scooter', 'mobility_scooter'), ('water_heater', 'water_heater'), ('electronic', 'electronic'), ('air_control', 'air_control')], max_length=128)),
                ('product_manufacturer', models.CharField(max_length=255)),
                ('product_brand', models.CharField(max_length=255)),
                ('product_SKU', models.CharField(max_length=32)),
                ('product_condition', models.CharField(choices=[('new', 'new'), ('refurbished', 'refurbished')], max_length=64)),
                ('product_in_stock', models.BooleanField(default=True)),
                ('product_quantity', models.IntegerField()),
                ('product_on_sale', models.BooleanField(default=False)),
                ('product_manuals_and_documentation', models.CharField(blank=True, max_length=128, null=True)),
                ('product_overview', jsonfield.fields.JSONField(blank=True, null=True)),
                ('product_features', jsonfield.fields.JSONField(blank=True, null=True)),
                ('product_specifications', jsonfield.fields.JSONField(blank=True, null=True)),
                ('product_warranty_additional_information', jsonfield.fields.JSONField(blank=True, null=True)),
                ('product_photos', models.CharField(blank=True, max_length=128, null=True)),
                ('product_videos', models.CharField(blank=True, max_length=128, null=True)),
                ('product_discounted', models.BooleanField(default=False)),
                ('product_discounted_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('product_package_contents', jsonfield.fields.JSONField(blank=True, null=True)),
                ('product_created_at', models.DateTimeField(auto_now_add=True)),
                ('product_updated_at', models.DateTimeField(auto_now=True)),
                ('stripe_product_id', models.CharField(blank=True, max_length=100, null=True)),
                ('product_count_in_user_cart', models.IntegerField(default=0)),
                ('product_in_user_cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('address', models.CharField(blank=True, max_length=64, null=True)),
                ('address_extended', models.CharField(blank=True, max_length=64, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('postal_code', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=128, null=True)),
                ('state_or_province', models.CharField(blank=True, max_length=128, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=128)),
                ('customer_email', models.CharField(max_length=128)),
                ('customer_question_text_body', models.TextField(blank=True, null=True)),
                ('company_answer_text_body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(default=None, max_length=255)),
                ('review_text_body', models.TextField(default=None)),
                ('picture_s3_url', models.CharField(blank=True, max_length=128, null=True)),
                ('video_s3_url', models.CharField(blank=True, max_length=128, null=True)),
                ('customer_name', models.CharField(default=None, max_length=128)),
                ('customer_email', models.CharField(default=None, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='GameConsole',
            fields=[
                ('baseproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.baseproduct')),
                ('game_console_classification_type', models.CharField(choices=[('PlayStation', 'PlayStation'), ('Xbox', 'Xbox'), ('Nintendo', 'Nintendo'), ('PC', 'PC'), ('Laptop', 'Laptop'), ('VR', 'VR')], max_length=64)),
            ],
            bases=('ecommerce.baseproduct',),
        ),
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('baseproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.baseproduct')),
                ('generator_classification_type', models.CharField(choices=[('portable', 'portable'), ('standby', 'standby'), ('inverter', 'inverter')], max_length=128)),
                ('generator_fuel_type', models.CharField(choices=[('gasoline', 'gasoline'), ('LP', 'LP'), ('Dual Fuel', 'Dual Fuel'), ('Diesel', 'Diesel'), ('Tri-Fuel', 'Tri-Fuel')], max_length=64)),
                ('generator_continuous_wattage_value', models.IntegerField()),
            ],
            bases=('ecommerce.baseproduct',),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_price_id', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.baseproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('address', models.CharField(blank=True, max_length=64, null=True)),
                ('address_extended', models.CharField(blank=True, max_length=64, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('postal_code', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=128, null=True)),
                ('state_or_province', models.CharField(blank=True, max_length=128, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
            ],
        ),
        migrations.AddField(
            model_name='baseproduct',
            name='product_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.productquestion'),
        ),
        migrations.AddField(
            model_name='baseproduct',
            name='product_reviews',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.productreview'),
        ),
        migrations.AddField(
            model_name='customer',
            name='product_count_FK',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.generator'),
        ),
    ]
