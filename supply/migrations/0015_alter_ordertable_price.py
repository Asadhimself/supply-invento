# Generated by Django 5.0.2 on 2024-03-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0014_ordertable_in_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='price',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
