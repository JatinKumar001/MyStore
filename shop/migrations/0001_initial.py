# Generated by Django 4.0.2 on 2022-07-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='buy/image')),
                ('date', models.DateField()),
            ],
        ),
    ]
