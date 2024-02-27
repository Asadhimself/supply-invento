# Generated by Django 5.0.2 on 2024-02-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Administrator'), ('Supplier', 'Supply Manager'), ('Storekeeper', 'Storekeeper'), ('Teacher', 'Teacher')], default='Teacher', max_length=20),
        ),
    ]
