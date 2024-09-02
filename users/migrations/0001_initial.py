# Generated by Django 5.1 on 2024-09-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
