# Generated by Django 5.0.2 on 2024-02-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0006_alter_ordertable_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='delivered_quantity',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
