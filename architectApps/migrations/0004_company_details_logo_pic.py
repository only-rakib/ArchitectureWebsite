# Generated by Django 3.1.1 on 2020-09-14 05:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('architectApps', '0003_auto_20200914_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='logo_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
