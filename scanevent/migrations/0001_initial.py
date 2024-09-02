# Generated by Django 5.1 on 2024-09-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_id', models.PositiveSmallIntegerField()),
                ('location', models.CharField(max_length=50)),
                ('drug_name', models.CharField(max_length=40)),
                ('batch_number', models.CharField(max_length=30)),
                ('pharmacy_id', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
