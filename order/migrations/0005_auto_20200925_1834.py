# Generated by Django 3.0.3 on 2020-09-25 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200923_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='product_name',
        ),
    ]
