# Generated by Django 3.1 on 2020-11-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0003_auto_20201104_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
