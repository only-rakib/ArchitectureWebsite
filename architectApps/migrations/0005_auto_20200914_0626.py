# Generated by Django 3.1.1 on 2020-09-14 06:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('architectApps', '0004_company_details_logo_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='company_description',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
