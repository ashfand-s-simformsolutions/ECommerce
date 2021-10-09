# Generated by Django 3.2.8 on 2021-10-09 05:23

import django.core.validators
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default=users.models.get_default_profile_image, max_length=255, null=True, upload_to=users.models.get_profile_image_filepath),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Enter valid Indian number', regex='^(\\+91[\\-\\s]?)?[0]?(91)?[789]\\d{9}$')]),
        ),
    ]