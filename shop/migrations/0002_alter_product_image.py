# Generated by Django 4.0.2 on 2022-07-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/image'),
        ),
    ]
