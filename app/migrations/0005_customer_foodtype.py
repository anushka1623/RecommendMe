# Generated by Django 3.1.3 on 2020-11-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201122_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='foodtype',
            field=models.CharField(choices=[('Veg', ' Veg'), ('NonVeg', 'NonVeg'), ('Both', 'Both')], max_length=300, null=True),
        ),
    ]
