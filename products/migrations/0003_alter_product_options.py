# Generated by Django 4.1.5 on 2024-04-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-id',)},
        ),
    ]
