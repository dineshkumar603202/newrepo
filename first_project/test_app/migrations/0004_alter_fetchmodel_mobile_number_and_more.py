# Generated by Django 4.0.1 on 2023-01-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_alter_fetchmodel_description_alter_fetchmodel_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fetchmodel',
            name='mobile_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fetchmodel',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
