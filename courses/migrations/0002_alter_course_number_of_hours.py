# Generated by Django 4.2.8 on 2023-12-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number_of_hours',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
