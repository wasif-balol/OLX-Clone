# Generated by Django 3.0.5 on 2020-04-26 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200426_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
