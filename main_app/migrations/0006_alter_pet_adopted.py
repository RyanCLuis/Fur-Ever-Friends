# Generated by Django 3.2.12 on 2024-01-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_pet_adopted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='Adopted',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=100),
        ),
    ]
