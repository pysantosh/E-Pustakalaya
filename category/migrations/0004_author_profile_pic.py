# Generated by Django 2.1 on 2018-09-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20180921_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(default='image', upload_to='images/authors/'),
        ),
    ]