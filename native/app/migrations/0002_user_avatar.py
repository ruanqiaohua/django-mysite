# Generated by Django 2.1.8 on 2019-06-03 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='avatar'),
            preserve_default=False,
        ),
    ]
