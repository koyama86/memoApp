# Generated by Django 4.2 on 2025-02-03 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shelf',
            old_name='category',
            new_name='tag',
        ),
    ]
