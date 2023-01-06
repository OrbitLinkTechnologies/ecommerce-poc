# Generated by Django 3.2 on 2023-01-05 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0023_auto_20230104_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseproduct',
            name='product_question',
        ),
        migrations.RemoveField(
            model_name='baseproduct',
            name='product_reviews',
        ),
        migrations.RemoveField(
            model_name='productquestion',
            name='company_answer_text_body',
        ),
        migrations.AddField(
            model_name='productquestion',
            name='base_product_association',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.baseproduct'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productreview',
            name='base_product_association',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.baseproduct'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productquestion',
            name='customer_question_text_body',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productreview',
            name='customer_email',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='customer_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review_text_body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review_title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='ProductAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_answer_text_body', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.productquestion')),
            ],
        ),
    ]
