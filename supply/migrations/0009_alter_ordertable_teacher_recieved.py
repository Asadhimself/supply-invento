# Generated by Django 5.0.2 on 2024-02-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0008_alter_ordertable_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='teacher_recieved',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
