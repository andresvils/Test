# Generated by Django 5.1.4 on 2025-05-31 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='creater_at',
            new_name='created_at',
        ),
    ]
