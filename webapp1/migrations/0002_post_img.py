# Generated by Django 2.2.7 on 2020-05-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='homepics'),
        ),
    ]
