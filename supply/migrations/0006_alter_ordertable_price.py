# Generated by Django 5.0.2 on 2024-02-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0005_alter_ordertable_teachers_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
    ]
