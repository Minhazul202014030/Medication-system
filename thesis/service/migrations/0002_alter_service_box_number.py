# Generated by Django 4.1.7 on 2023-10-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='box_number',
            field=models.PositiveIntegerField(),
        ),
    ]
