# Generated by Django 5.0.1 on 2024-01-22 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_delete_dog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='breed',
            new_name='species',
        ),
    ]
