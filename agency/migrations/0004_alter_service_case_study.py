# Generated by Django 5.2.1 on 2025-06-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_alter_contact_options_alter_package_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='case_study',
            field=models.FileField(blank=True, null=True, upload_to='case_studies'),
        ),
    ]
