# Generated by Django 3.2.7 on 2021-09-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveBigIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True),
        ),
    ]
