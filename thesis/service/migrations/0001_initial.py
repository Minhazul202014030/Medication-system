# Generated by Django 4.1.7 on 2023-10-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_number', models.PositiveIntegerField(unique=True)),
                ('medicine_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
