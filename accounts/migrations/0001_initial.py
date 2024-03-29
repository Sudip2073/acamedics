# Generated by Django 3.1.4 on 2021-04-04 13:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sid', models.IntegerField(validators=[django.core.validators.MinValueValidator(180000), django.core.validators.MaxValueValidator(1901000)])),
                ('enrollement', models.CharField(choices=[('E', 'BSc. (Hons) Ethical Hacking And Cybersecurity'), ('CS', 'BSc. (Hons) Computing')], max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('batch', models.CharField(max_length=5)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
