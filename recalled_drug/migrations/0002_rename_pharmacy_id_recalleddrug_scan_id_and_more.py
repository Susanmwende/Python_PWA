# Generated by Django 5.1 on 2024-09-05 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recalled_drug', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recalleddrug',
            old_name='pharmacy_id',
            new_name='scan_id',
        ),
        migrations.RemoveField(
            model_name='recalleddrug',
            name='batch_number',
        ),
        migrations.RemoveField(
            model_name='recalleddrug',
            name='drug_name',
        ),
    ]
