# Generated by Django 5.1.2 on 2024-11-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(default='2024-01-01', verbose_name='Дата производства'),
        ),
    ]
