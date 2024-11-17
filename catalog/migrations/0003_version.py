# Generated by Django 5.1.2 on 2024-11-14 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_view_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=20)),
                ('version_name', models.CharField(max_length=255)),
                ('is_current', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product')),
            ],
        ),
    ]
