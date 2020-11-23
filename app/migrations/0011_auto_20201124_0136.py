# Generated by Django 3.1.3 on 2020-11-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201124_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
