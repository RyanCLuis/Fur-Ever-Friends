# Generated by Django 3.2.12 on 2024-01-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_pet_fixed'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='Adopted',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=100),
        ),
    ]
