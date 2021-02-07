# Generated by Django 3.1.4 on 2021-01-16 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='mod_code',
            field=models.CharField(default=1, max_length=9, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(3)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modules',
            name='year',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100),
        ),
    ]
