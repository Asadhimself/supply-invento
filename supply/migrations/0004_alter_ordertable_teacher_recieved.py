# Generated by Django 5.0.2 on 2024-02-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0003_alter_ordertable_delivered_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='teacher_recieved',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
    ]
