# Generated by Django 4.1.5 on 2024-04-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_saved_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='avatars/favicon.png', upload_to='avatars/'),
        ),
    ]
