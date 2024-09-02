# Generated by Django 5.1 on 2024-09-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_id', models.PositiveSmallIntegerField()),
                ('pharmacy_name', models.CharField(max_length=15)),
                ('registration_number', models.PositiveSmallIntegerField()),
                ('license_status', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=20)),
                ('town', models.CharField(max_length=20)),
            ],
        ),
    ]
