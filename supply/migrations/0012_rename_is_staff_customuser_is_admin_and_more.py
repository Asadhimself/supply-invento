# Generated by Django 5.0.2 on 2024-03-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0011_customuser_first_name_customuser_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_staff',
            new_name='is_admin',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]